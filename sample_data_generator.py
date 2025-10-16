import sys
sys.path.append('database')
from database.db_operations import DatabaseManager
import random
from datetime import datetime, timedelta

def generate_sample_data():
    try:
        db = DatabaseManager()
    except Exception as e:
        print(f"Database connection failed: {e}")
        print("Make sure PostgreSQL is running and database 'planeteye' exists")
        return False
    
    # Sample object types and their typical confidence ranges
    objects = [
        ('car', 0.7, 0.95),
        ('person', 0.6, 0.9),
        ('bicycle', 0.5, 0.85),
        ('truck', 0.65, 0.9),
        ('bus', 0.7, 0.95)
    ]
    
    # Generate 100 sample detections
    for i in range(100):
        obj_type, min_conf, max_conf = random.choice(objects)
        confidence = round(random.uniform(min_conf, max_conf), 3)
        
        # NYC area coordinates
        lat = round(random.uniform(40.7, 40.8), 6)
        lon = round(random.uniform(-74.0, -73.9), 6)
        
        db.insert_detection(
            object_type=obj_type,
            confidence=confidence,
            image_path=f"sample_image_{i}.jpg",
            lat=lat,
            lon=lon
        )
    
    print("Generated 100 sample detections")
    db.close()
    return True

if __name__ == "__main__":
    generate_sample_data()