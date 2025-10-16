#!/usr/bin/env python3
"""
Main script to run the complete AI-powered data logging system
"""
import subprocess
import sys
import os

def run_command(command, description):
    print(f"\n{'='*50}")
    print(f"STEP: {description}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"✗ Error in {description}: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
        return False
    return True

def main():
    print("AI-POWERED DATA LOGGING SYSTEM")
    print("Starting automated setup and execution...")
    
    # Change to database directory for setup
    os.chdir('database')
    
    # Setup database
    if not run_command("python setup_db.py", "Database Setup"):
        return
    
    # Go back to root
    os.chdir('..')
    
    # Generate sample data
    if not run_command("python sample_data_generator.py", "Sample Data Generation"):
        return
    
    # Run analysis
    os.chdir('analysis')
    if not run_command("python queries.py", "Data Analysis"):
        return
    
    print(f"\n{'='*50}")
    print("✓ SYSTEM EXECUTION COMPLETED SUCCESSFULLY!")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()