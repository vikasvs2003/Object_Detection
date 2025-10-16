import os
import sys
sys.path.append('../database')

from ultralytics import YOLO
import cv2
from datetime import datetime

# Import from local database directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'database'))
from db_operations import DatabaseManager

class ObjectDetector:
    def __init__(self):
        self.model = YOLO('yolov8n.pt')  # Lightweight model
        self.db = DatabaseManager()
    
    def detect_from_image(self, image_path):
        # ✅ Step 1: Ensure image can be read
        img = cv2.imread(image_path)
        if img is None:
            print(f"⚠️ Image Read Error: {image_path}")
            return []  # Skip unreadable files safely

        # ✅ Step 2: Run YOLO detection
        try:
            results = self.model(image_path)
        except Exception as e:
            print(f"❌ YOLO failed on {image_path}: {e}")
            return []

        detections = []
        for result in results:
            boxes = result.boxes
            if boxes is not None:
                for box in boxes:
                    class_id = int(box.cls[0])
                    confidence = float(box.conf[0])
                    class_name = self.model.names.get(class_id, "Unknown")
                    
                    if confidence > 0.5:  # Filter low confidence
                        detections.append({
                            'object_type': class_name,
                            'confidence': confidence,
                            'image_path': image_path
                        })
        
        return detections
    
    def detect_from_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        all_detections = []
        frame_count = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            frame_count += 1
            if frame_count % 30 == 0:  # Process every 30th frame
                temp_path = f"temp_frame_{frame_count}.jpg"
                cv2.imwrite(temp_path, frame)
                
                detections = self.detect_from_image(temp_path)
                for detection in detections:
                    detection['image_path'] = f"{video_path}_frame_{frame_count}"
                    self.db.insert_detection(**detection)
                    all_detections.append(detection)
                
                os.remove(temp_path)
        
        cap.release()
        return all_detections
    
    def process_directory(self, directory_path):
        all_detections = []
        
        if not os.path.exists(directory_path):
            print(f"❌ Directory not found: {directory_path}")
            return []

        for filename in os.listdir(directory_path):
            filepath = os.path.join(directory_path, filename)
            
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                print(f"🖼️ Processing image: {filename}")
                detections = self.detect_from_image(filepath)
                all_detections.extend(detections)
                
                for detection in detections:
                    self.db.insert_detection(**detection)
                    
            elif filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
                print(f"🎥 Processing video: {filename}")
                detections = self.detect_from_video(filepath)
                all_detections.extend(detections)
            else:
                print(f"⏭️ Skipping file: {filename}")
        
        print(f"\n✅ Processed {len(all_detections)} detections total.")
        return all_detections

if __name__ == "__main__":
    detector = ObjectDetector()
    detector.process_directory(r"D:\PLANETEYE\sample_images")  # ✅ Use absolute path
    detector.db.close()
