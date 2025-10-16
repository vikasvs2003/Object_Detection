import sys
sys.path.append('database')
import psycopg2
from config import DB_CONFIG

def view_stored_data():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # Total count
    cur.execute("SELECT COUNT(*) FROM detections")
    total = cur.fetchone()[0]
    print(f"Total detections stored: {total}")
    
    # Recent detections
    cur.execute("""
        SELECT d.object_id, COALESCE(d.object_name, ot.type_name) as object_name, 
               d.confidence_score, d.image_reference, d.timestamp, d.latitude, d.longitude
        FROM detections d 
        LEFT JOIN object_types ot ON d.type_id = ot.type_id 
        ORDER BY d.object_id DESC 
        LIMIT 20
    """)
    
    print("\nRecent 20 detections:")
    print("-" * 100)
    print(f"{'ID':<5} | {'OBJECT NAME':<15} | {'CONFIDENCE':<10} | {'IMAGE':<20} | {'COORDINATES':<20}")
    print("-" * 100)
    for row in cur.fetchall():
        coords = f"({row[5]:.3f}, {row[6]:.3f})"
        print(f"{row[0]:<5} | {row[1]:<15} | {row[2]:<10.3f} | {row[3]:<20} | {coords:<20}")
    
    conn.close()

if __name__ == "__main__":
    view_stored_data()