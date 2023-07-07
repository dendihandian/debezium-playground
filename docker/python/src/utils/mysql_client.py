from pymysql.cursors import DictCursor
from pymysql import connect
from os import getenv

MYSQL_HOST = getenv('MYSQL_HOST')
MYSQL_USER = getenv('MYSQL_USER')
MYSQL_PASS = getenv('MYSQL_PASSWORD')

mysql_conn = connect(
    host=MYSQL_HOST, 
    user=MYSQL_USER, 
    password=MYSQL_PASS, 
    database='debezium_playground', 
    cursorclass=DictCursor,
)