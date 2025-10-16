import sys
sys.path.append('database')
import psycopg2
from config import DB_CONFIG

def show_detected_objects():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # Show all unique object types detected
    cur.execute("""
        SELECT DISTINCT object_name, COUNT(*) as count
        FROM detections 
        WHERE object_name IS NOT NULL
        GROUP BY object_name
        ORDER BY count DESC
    """)
    
    print("DETECTED OBJECT TYPES:")
    print("=" * 40)
    for row in cur.fetchall():
        print(f"* {row[0]:<15} : {row[1]:>3} detections")
    
    # Show recent detections by object type
    print("\nRECENT DETECTIONS BY TYPE:")
    print("=" * 60)
    
    cur.execute("""
        SELECT object_name, confidence_score, image_reference
        FROM detections 
        WHERE object_name IS NOT NULL
        ORDER BY object_id DESC 
        LIMIT 15
    """)
    
    for row in cur.fetchall():
        image_name = row[2].split('\\')[-1] if '\\' in row[2] else row[2]
        print(f"- {row[0]:<12} | Confidence: {row[1]:.3f} | Image: {image_name}")
    
    conn.close()

if __name__ == "__main__":
    show_detected_objects()