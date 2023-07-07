from utils.mysql_client import mysql_conn
from faker import Faker
from datetime import datetime
from faker.providers import date_time
from faker.providers import lorem

# Create a cursor object to execute SQL queries
cursor = mysql_conn.cursor()

# Check if a database exists
cursor.execute(f"SHOW DATABASES")

# Fetch the result
result = cursor.fetchall()

print(result)

# Close the cursor and connection
cursor.close()
mysql_conn.close()

"""
docker-compose exec python python mysql_show_databases.py
"""