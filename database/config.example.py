import os

# Example database configuration
# Copy this file to config.py and update with your credentials

DB_CONFIG = {
    'host': 'localhost',
    'database': 'planeteye',
    'user': 'postgres',
    'password': 'your_postgres_password_here',  # Update this
    'port': 5432
}

# Alternative: Use environment variables
# DB_CONFIG = {
#     'host': os.getenv('DB_HOST', 'localhost'),
#     'database': os.getenv('DB_NAME', 'planeteye'),
#     'user': os.getenv('DB_USER', 'postgres'),
#     'password': os.getenv('DB_PASSWORD', 'your_password'),
#     'port': int(os.getenv('DB_PORT', 5432))
# }