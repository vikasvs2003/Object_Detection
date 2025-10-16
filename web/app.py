import sys
sys.path.append('../database')
from flask import Flask, render_template
import psycopg2
from config import DB_CONFIG

app = Flask(__name__)

@app.route('/')
def dashboard():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # Get object summary
    cur.execute("""
        SELECT object_name, COUNT(*) as count, AVG(confidence_score) as avg_conf
        FROM detections 
        WHERE object_name IS NOT NULL
        GROUP BY object_name
        ORDER BY count DESC
    """)
    summary = cur.fetchall()
    
    # Get recent detections
    cur.execute("""
        SELECT object_name, confidence_score, image_reference, timestamp
        FROM detections 
        WHERE object_name IS NOT NULL
        ORDER BY object_id DESC 
        LIMIT 50
    """)
    recent = cur.fetchall()
    
    conn.close()
    return render_template('dashboard.html', summary=summary, recent=recent)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)