import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  database = "school",
  user = "root",
  password = "8381962255"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for i in mycursor:
    print(i)
