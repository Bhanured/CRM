import mysql.connector
dataBase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bhanu@123",
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS bhanuco")
cursorObject.close()
dataBase.close()
print("ALL DONE!")