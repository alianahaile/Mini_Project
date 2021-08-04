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


sql = "INSERT INTO products (product_name, price) VALUES (%s, %s)"

val = [
  ('Tea', 1.05),
  ('Espresso',1.25),
  ('Tea',2.50),
  ('Cold Brew',2.05),
  ('Latte',1.50),
  ('Cappuccino',1.25),
  ('Hot Chocolate',2.00)
]

cursor.executemany(sql, val)


cursor.execute('SELECT product_name,  price FROM products')

# Gets all rows from the result
rows = cursor.fetchall()
for row in rows:
    # print(row)
    print(f'\n Product_Name: {str(row[0])}, Price: {row[1]},')


connection.commit()
cursor.close()
connection.close()