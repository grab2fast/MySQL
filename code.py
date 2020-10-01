import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  database = "school",
  user = "root",
  password = "8381962255"
)

mycursor = mydb.cursor()

#sql = "INSERT INTO students(First_Name, Last_Name, Class, Address)  VALUES(%s, %s, %s, %s)"
#val = []


#mycursor.executemany(sql,val)

#mydb.commit()
#print(mycursor.rowcount, "Record Inserted")

mycursor.execute("SHOW TABLES")

for i in mycursor:
    print(i)
