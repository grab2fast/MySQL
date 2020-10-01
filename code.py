import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",                  # Host address
  database = "database",               # Database name
  user = "root",                       # Username
  password = "password"                # Password
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for i in mycursor:
    print(i)
