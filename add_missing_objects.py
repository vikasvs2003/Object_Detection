import sys
sys.path.append('database')
import psycopg2
from config import DB_CONFIG

def add_missing_object_types():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # Add missing object types that YOLO can detect
    missing_objects = ['handbag', 'tv', 'laptop', 'cell phone', 'book', 'clock', 'chair', 'dining table']
    
    for obj in missing_objects:
        cur.execute("INSERT INTO object_types (type_name) VALUES (%s) ON CONFLICT (type_name) DO NOTHING", (obj,))
    
    conn.commit()
    print(f"Added {len(missing_objects)} object types to database")
    
    # Show all object types now
    cur.execute("SELECT type_name FROM object_types ORDER BY type_name")
    print("\nAll available object types:")
    for row in cur.fetchall():
        print(f"- {row[0]}")
    
    conn.close()

if __name__ == "__main__":
    add_missing_object_types()