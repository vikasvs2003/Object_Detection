#!/usr/bin/env python3
"""
Quick demo of the system using sample data (no AI required)
"""
import sys
import os

# Add database path
sys.path.append('database')

def main():
    print("=== AI-POWERED DATA LOGGING SYSTEM DEMO ===\n")
    
    # Step 1: Setup Database
    print("Step 1: Setting up database...")
    os.chdir('database')
    
    try:
        from setup_db import setup_database
        setup_database()
        print("✓ Database setup completed\n")
    except Exception as e:
        print(f"✗ Database setup failed: {e}")
        print("Make sure PostgreSQL is installed and running")
        return
    
    os.chdir('..')
    
    # Step 2: Generate Sample Data
    print("Step 2: Generating sample detection data...")
    try:
        from sample_data_generator import generate_sample_data
        generate_sample_data()
        print("✓ Sample data generated\n")
    except Exception as e:
        print(f"✗ Sample data generation failed: {e}")
        return
    
    # Step 3: Run Analysis
    print("Step 3: Running data analysis...")
    os.chdir('analysis')
    
    try:
        from queries import QueryAnalyzer
        analyzer = QueryAnalyzer()
        analyzer.generate_report()
        print("✓ Analysis completed successfully!")
    except Exception as e:
        print(f"✗ Analysis failed: {e}")
        return
    
    print("\n" + "="*50)
    print("✓ DEMO COMPLETED SUCCESSFULLY!")
    print("The system is working with sample data.")
    print("To use real AI detection, add images to sample_images/ folder")
    print("and run: python ai/detect_objects.py")
    print("="*50)

if __name__ == "__main__":
    main()