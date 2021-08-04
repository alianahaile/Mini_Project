import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
)


cursor = connection.cursor()


sql = "INSERT INTO couriers (courier_name, phone_number) VALUES (%s, %s)"

val = [
  ('Haben', '+447582171134'),
  ('Omega','+447709779632'),
  ('Yuel','+447416273936'),
  ('Milen','+447350812767'),
  ('Mary','+447457466901'),
]

cursor.executemany(sql, val)


cursor.execute('SELECT courier_name, phone_number FROM couriers')

# Gets all rows from the result
rows = cursor.fetchall()
for row in rows:
    # print(row)
    print(f'\n Courier_Name: {str(row[0])}, Phone_Number: {row[1]},')

connection.commit()
cursor.close()
connection.close()