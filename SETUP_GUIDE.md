# 🚀 Quick Setup Guide

## Prerequisites Checklist
- [ ] Python 3.8+ installed
- [ ] PostgreSQL installed and running
- [ ] Git installed (for cloning)

## 5-Minute Setup

### 1. Clone & Install
```bash
git clone https://github.com/yourusername/planeteye-ai-detection.git
cd planeteye-ai-detection
pip install -r requirements.txt
```

### 2. Database Setup
```bash
# Create PostgreSQL database
createdb planeteye

# Copy config file and update password
cp database/config.example.py database/config.py
# Edit database/config.py with your PostgreSQL password

# Initialize database
cd database
python setup_db.py
```

### 3. Test with Sample Data
```bash
# Generate sample detections
python sample_data_generator.py

# Start web dashboard
python start_web_ui.py

# Open: http://localhost:5000
```

### 4. Run AI Detection
```bash
# Add images/videos to sample_images/ folder
# Run detection
cd ai
python detect_objects.py

# View results on web dashboard (auto-refreshes)
```

## Troubleshooting

### Database Connection Error
```bash
# Check PostgreSQL is running
pg_ctl status

# Verify database exists
psql -l | grep planeteye
```

### YOLOv8 Model Download
```bash
# Model downloads automatically on first run
# If issues, manually download:
cd ai
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

### Web UI Not Loading
```bash
# Check Flask is installed
pip install flask

# Verify port 5000 is free
netstat -an | grep 5000
```

## Quick Commands Reference

```bash
# Start web dashboard
python start_web_ui.py

# Run AI detection
cd ai && python detect_objects.py

# View detection stats
python show_detected_objects.py

# Generate sample data
python sample_data_generator.py

# Database queries
cd analysis && python queries.py
```

## File Structure After Setup
```
PLANETEYE/
├── ai/yolov8n.pt              # Downloaded AI model
├── database/config.py         # Your DB credentials
├── sample_images/             # Your images/videos
└── screenshots/               # Add your screenshots
```

✅ **Setup Complete!** Your AI detection system is ready to use.