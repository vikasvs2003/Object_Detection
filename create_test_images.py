import cv2
import numpy as np
import os

def create_realistic_test_images():
    os.makedirs('sample_images', exist_ok=True)
    
    # Image 1: Simple car-like rectangle
    img1 = np.ones((480, 640, 3), dtype=np.uint8) * 200  # Light gray background
    # Draw car body (dark rectangle)
    cv2.rectangle(img1, (200, 250), (440, 350), (50, 50, 50), -1)
    # Draw wheels (circles)
    cv2.circle(img1, (240, 350), 25, (0, 0, 0), -1)
    cv2.circle(img1, (400, 350), 25, (0, 0, 0), -1)
    # Draw windows
    cv2.rectangle(img1, (220, 260), (420, 310), (100, 150, 200), -1)
    cv2.imwrite('sample_images/car_test.jpg', img1)
    
    # Image 2: Person-like figure
    img2 = np.ones((480, 640, 3), dtype=np.uint8) * 220  # Light background
    # Draw person (stick figure style but more filled)
    # Head
    cv2.circle(img2, (320, 150), 40, (200, 180, 160), -1)
    # Body
    cv2.rectangle(img2, (300, 190), (340, 320), (100, 100, 200), -1)
    # Arms
    cv2.rectangle(img2, (260, 200), (300, 220), (100, 100, 200), -1)
    cv2.rectangle(img2, (340, 200), (380, 220), (100, 100, 200), -1)
    # Legs
    cv2.rectangle(img2, (305, 320), (320, 400), (50, 50, 150), -1)
    cv2.rectangle(img2, (325, 320), (340, 400), (50, 50, 150), -1)
    cv2.imwrite('sample_images/person_test.jpg', img2)
    
    # Image 3: Bicycle-like shape
    img3 = np.ones((480, 640, 3), dtype=np.uint8) * 210
    # Draw bicycle wheels
    cv2.circle(img3, (200, 300), 60, (0, 0, 0), 5)
    cv2.circle(img3, (440, 300), 60, (0, 0, 0), 5)
    # Draw frame
    cv2.line(img3, (200, 300), (320, 200), (100, 100, 100), 8)
    cv2.line(img3, (320, 200), (440, 300), (100, 100, 100), 8)
    cv2.line(img3, (260, 250), (380, 250), (100, 100, 100), 6)
    cv2.imwrite('sample_images/bicycle_test.jpg', img3)
    
    print("Created 3 realistic test images:")
    print("- car_test.jpg")
    print("- person_test.jpg") 
    print("- bicycle_test.jpg")

if __name__ == "__main__":
    create_realistic_test_images()