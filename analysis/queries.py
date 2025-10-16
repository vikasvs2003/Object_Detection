import sys
sys.path.append('../database')
import psycopg2
from config import DB_CONFIG
import pandas as pd

class QueryAnalyzer:
    def __init__(self):
        self.conn = psycopg2.connect(**DB_CONFIG)
    
    def detections_per_type(self):
        query = """
        SELECT ot.type_name, COUNT(*) as detection_count
        FROM detections d
        JOIN object_types ot ON d.type_id = ot.type_id
        GROUP BY ot.type_name
        ORDER BY detection_count DESC;
        """
        return pd.read_sql(query, self.conn)
    
    def detections_by_date_range(self, start_date, end_date):
        query = """
        SELECT ot.type_name, d.timestamp, d.confidence_score
        FROM detections d
        JOIN object_types ot ON d.type_id = ot.type_id
        WHERE d.timestamp BETWEEN %s AND %s
        ORDER BY d.timestamp;
        """
        return pd.read_sql(query, self.conn, params=[start_date, end_date])
    
    def detections_by_location(self, min_lat, max_lat, min_lon, max_lon):
        query = """
        SELECT ot.type_name, d.latitude, d.longitude, d.confidence_score
        FROM detections d
        JOIN object_types ot ON d.type_id = ot.type_id
        WHERE d.latitude BETWEEN %s AND %s
        AND d.longitude BETWEEN %s AND %s;
        """
        return pd.read_sql(query, self.conn, params=[min_lat, max_lat, min_lon, max_lon])
    
    def highest_confidence_per_type(self):
        query = """
        SELECT ot.type_name, MAX(d.confidence_score) as max_confidence
        FROM detections d
        JOIN object_types ot ON d.type_id = ot.type_id
        GROUP BY ot.type_name
        ORDER BY max_confidence DESC;
        """
        return pd.read_sql(query, self.conn)
    
    def generate_report(self):
        print("=== DETECTION ANALYSIS REPORT ===\n")
        
        print("1. Detections per Object Type:")
        print(self.detections_per_type())
        print("\n" + "="*50 + "\n")
        
        print("2. Highest Confidence per Type:")
        print(self.highest_confidence_per_type())
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    analyzer = QueryAnalyzer()
    analyzer.generate_report()