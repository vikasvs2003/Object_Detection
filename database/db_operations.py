import psycopg2
from config import DB_CONFIG
from datetime import datetime
import random

class DatabaseManager:
    def __init__(self):
        self.conn = psycopg2.connect(**DB_CONFIG)
        self.cur = self.conn.cursor()
    
    def get_type_id(self, object_type):
        self.cur.execute("SELECT type_id FROM object_types WHERE type_name = %s", (object_type,))
        result = self.cur.fetchone()
        return result[0] if result else None
    
    def insert_detection(self, object_type, confidence, image_path, lat=None, lon=None):
        type_id = self.get_type_id(object_type)
        if not type_id:
            return False
        
        # Simulate coordinates if not provided
        if lat is None:
            lat = round(random.uniform(40.0, 41.0), 6)  # NYC area
        if lon is None:
            lon = round(random.uniform(-74.5, -73.5), 6)
        
        self.cur.execute("""
            INSERT INTO detections (type_id, object_name, confidence_score, image_reference, latitude, longitude)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (type_id, object_type, confidence, image_path, lat, lon))
        
        self.conn.commit()
        return True
    
    def batch_insert(self, detections):
        for detection in detections:
            self.insert_detection(**detection)
    
    def close(self):
        self.conn.close()