import sys
sys.path.append('ai')
from detect_objects import ObjectDetector

def test_video():
    detector = ObjectDetector()
    
    # Test with existing video file
    video_files = ['sample_images/istockphoto-999135014-640_adpp_is.mp4']
    
    for video_file in video_files:
        print(f"Testing video: {video_file}")
        detections = detector.detect_from_video(video_file)
        print(f"Found {len(detections)} detections in video")
    
    detector.db.close()

if __name__ == "__main__":
    test_video()