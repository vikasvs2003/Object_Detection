import psycopg2
from config import DB_CONFIG

def setup_database():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # Read and execute schema
        with open('schema.sql', 'r') as f:
            cur.execute(f.read())
        
        conn.commit()
        print("Database setup completed successfully!")
        
    except Exception as e:
        print(f"Error setting up database: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    setup_database()