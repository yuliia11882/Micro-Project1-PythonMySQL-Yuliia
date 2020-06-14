#step 1  importing MySQL connector package
import mysql.connector

#step 2  create connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd='Root',

  database ='PyDB_Demo'
)
#step 3  creating cursor
mycursor = mydb.cursor()

# Delete Record
query = 'DELETE FROM employees WHERE job_title ="Graphic Designer"'
mycursor.execute(query)

##apply the changes
mydb.commit()


print(mycursor.rowcount, "record(s) deleted")









#_________________________________________________________________________
#fetchall()    method,  fetches all rows from the last executed statement
#result = mycursor.fetchall()


#__________________________________________________
#or:
# print(mycursor.rowcount, "record(s) deleted")
# mycursor.execute('SELECT * FROM employees')
# for record in mycursor:
#__________________________________________________



#for thiso in result:
#   print('__________________________________')
#   print("ID:", thiso[0])
#   print('First Name: ', thiso[1])
#   print('Last Name: ', thiso[2])
#   print('Email: ', thiso[3])
#  print('Job Title: ', thiso[4])
#  print('Date Hired: ', thiso[5])
#   print('Salary: ', thiso[6])
#  print('__________________________________')
