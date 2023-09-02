import os
import psycopg2

# Read environment variables
telegram_api_key = os.environ.get("TELEGRAM_API_KEY")
database_uri = os.environ.get("DATABASE_URI")

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(postgres://epusmlirevfjmr:2fed1e715c73d95006c8e2be06b8b3858367e0ef6e9108096cf767af4a28b96d@ec2-3-217-146-37.compute-1.amazonaws.com:5432/d31e8rvj3ul73q
)
except Exception as e:
    print(f"Error: Unable to connect to the database. {e}")
    exit(1)

# db_operations.py

import os
import psycopg2
import settings  # Assuming settings.py is your main settings file

def connect_db():
    conn = psycopg2.connect(settings.postgres://epusmlirevfjmr:2fed1e715c73d95006c8e2be06b8b3858367e0ef6e9108096cf767af4a28b96d@ec2-3-217-146-37.compute-1.amazonaws.com:5432/d31e8rvj3ul73q)
    return conn
