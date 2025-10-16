# Setup Instructions

## 1. Install PostgreSQL
- Download from: https://www.postgresql.org/download/windows/
- During installation, remember your password for 'postgres' user
- Default port: 5432

## 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

## 3. Database Setup
1. Open pgAdmin or psql
2. Create database: `CREATE DATABASE planeteye;`
3. Run: `python database/setup_db.py`

## 4. Run Object Detection
```bash
python ai/detect_objects.py --image_path sample_images/
```

## 5. Run Analysis
```bash
python analysis/queries.py
```