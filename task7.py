#step 1  importing MySQL connector package
import mysql.connector

#step 2  create connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd='root',

  database ='PyDB_Demo'
)
#step 3  creating cursor
mycursor = mydb.cursor()


#backup the database 'PyDB_Demo' using MySQL Workbench

#Delete/Drop database using DROP DATABASE
mycursor.execute('DROP DATABASE IF EXISTS PyDB_Demo')

#restore database 'PyDB_Demo' using MySQL Workbench