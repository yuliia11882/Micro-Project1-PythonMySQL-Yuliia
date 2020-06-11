#step 1  importing MySQL connector package
import mysql.connector

#step 2  create connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password='root1',

  database ='PyDB_Demo'
)
#step 3  creating cursor
mycursor = mydb.cursor()



#insert records
query = 'INSERT INTO employees (first_name, last_name, email, job_title, date_hired, salary) VALUES (%s,%s,%s,%s,%s,%s)'
values = [
    ('abcd', 'Green', 'gree@gmail01.com', 'HR Manager', '2019-01-07', 48000),
    ('efgh', 'Yellow', 'yell@gmail02.com', 'Web Developer', '2019-01-07', 45000),
    ('ijkl', 'Purple', 'purp@gmail03.com', 'Graphic Designer', '2019-01-07', 35000)
]

#insert many rows into table    executemany() method
mycursor.executemany(query, values)

#apply the changes
mydb.commit()



#display all records
result = mycursor.fetchall()

mycursor.execute("SELECT * FROM employees")
for row in result:
  print(row)