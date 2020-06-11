
#step 1  importing MySQL connector package
import mysql.connector

#step 2  create connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password='root1',
 
)
#step 3  creating cursor
mycursor = mydb.cursor()


#creating database
mycursor.execute ("CREATE DATABASE PyDB_Demo")
#using current database
mycursor.execute ("USE  PyDB_Demo")

#creating table    employees
mycursor.execute("CREATE TABLE employees  (emp_id INT PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(40) NOT NULL, last_name VARCHAR(40) NOT NULL, email VARCHAR(50) NOT NULL UNIQUE, job_title VARCHAR(40) NOT NULL, date_hired DATE NOT NULL, salary DEC CHECK ( salary >= 15,000 AND salary <= 50,000) ))")

#showing all tables
mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)


