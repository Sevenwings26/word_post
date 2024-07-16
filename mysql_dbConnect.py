import mysql.connector

myBD = mysql.connector.connect(
    host="localhost",
    user="root",
    password="iarowosola9876#+",
    database="word_site_database",
    auth_plugin='mysql_native_password'
)


myCursor = myBD.cursor()
# print("connected")

# create database 
myCursor.execute("CREATE DATABASE word_site_database")
print("Database Created...")