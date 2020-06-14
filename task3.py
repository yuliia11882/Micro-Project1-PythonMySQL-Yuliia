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




# example0 
mycursor.execute('SELECT * FROM employees ORDER BY first_name')

result = mycursor.fetchall()


for record in result:
    print('______________________________________')
    print('ID: ', record[0])
    print('First name: ', record[1])
    print('Last name: ', record[2])
    print('Email: ', record[3])
    print('Job Title: ', record[4])
    print('Date Hired: ', record[5])
    print('Salary: ', record[6])
    print('______________________________________')




#example1
query = "SELECT * FROM clients WHERE last_name LIKE 'p%'"
mycursor.execute(query)


result = mycursor.fetchall()

   
for record in result:
    
    print('__________________________________')
    print("ID: ", record[0])
    print('First Name: ', record[1])
    print('Last Name: ', record[2])
    print('Email: ', record[3])
    print('Job Title: ', record[4])
    print('Date Hired: ', record[5])
    print('Salary: ', record[6])
    print('__________________________________')




#example2

mycursor.execute("SELECT * FROM employees WHERE Salary<45000")


result =mycursor.fetchall()

for record in result:
   
    print('______________________________________')
    print("ID: ", record[0])
    print('First Name: ', record[1])
    print('Last Name: ', record[2])
    print('Email: ', record[3])
    print('Job Title: ', record[4])
    print('Date Hired: ', record[5])
    print('Salary: ', record[6])
    print('______________________________________')





#example3

query = "SELECT * FROM employees WHERE first_name LIKE 'i%' OR last_name LIKE 'g%'"
mycursor.execute(query)

result = mycursor.fetchall()

for this in result: 
    
    print('__________________________________')
    print("ID: ", this[0])
    print('First Name: ', this[1])
    print('Last Name: ', this[2])
    print('Email: ', this[3])
    print('Job Title: ', this[4])
    print('Date Hired: ', this[5])
    print('Salary: ', this[6])
    print('__________________________________')




#example4

query = "SELECT * FROM employees WHERE  last_name LIKE 'y%' AND job_title LIKE 'w%"
mycursor.execute(query)

result = mycursor.fetchall()

for thisWat in result: 
  
    print('__________________________________')
    print("ID: ", thisWat[0])
    print('First Name: ', thisWat[1])
    print('Last Name: ', thisWat[2])
    print('Email: ', thisWat[3])
    print('Job Title: ', thisWat[4])
    print('Date Hired: ', thisWat[5])
    print('Salary: ', thisWat[6])
    print('__________________________________')
