import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="heart_segmentation_db",
    user=os.environ['archdev'],
    password=os.environ['archdev']
)

# Open a cursor to perform database operations
cur = conn.cursor()