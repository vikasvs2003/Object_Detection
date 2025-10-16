#!/usr/bin/env python3
import subprocess
import sys
import os

def start_web_ui():
    print("🌐 Starting AI Object Detection Web UI...")
    print("📍 URL: http://localhost:5000")
    print("🔄 Press Ctrl+C to stop")
    print("-" * 50)
    
    # Change to web directory
    os.chdir('web')
    
    try:
        # Start Flask app
        subprocess.run([sys.executable, 'app.py'], check=True)
    except KeyboardInterrupt:
        print("\n✅ Web UI stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure Flask is installed: pip install flask")

if __name__ == "__main__":
    start_web_ui()