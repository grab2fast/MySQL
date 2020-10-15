import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",                  # Host address
  database = "database",               # Database name
  user = "root",                       # Username
  password = "password"                # Password
)

mycursor = mydb.cursor()

mycursor.execute("Create Table") # Table Name

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
