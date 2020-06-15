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



#backup copy employees table first. csv.

#Delete table using DROP TABLE
mycursor.execute('DROP TABLE IF EXISTS PyDB_Demo.employees')
#done

#restore table employees from backup copy