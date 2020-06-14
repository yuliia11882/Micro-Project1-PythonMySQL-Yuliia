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





#insert records
query = "UPDATE employees SET first_name ='mnop', last_name='Red', email='red@gmail00.com' WHERE emp_id=1" 
mycursor.execute(query)


#apply the changes
mydb.commit()


print(mycursor.rowcount, "record(s) affected")











#___________________________________________________________________________
#fetchall()    method,  fetches all rows from the last executed statement
#result = mycursor.fetchall()



#_____________________________________________________________________________________________________________
#or:

# print(mycursor.rowcount, "record(s) updated")
# mycursor.execute('SELECT * FROM employees')
# for thiswot in mycursor:



#for thiswot in result:
    
#    print('__________________________________')
#    print("ID: ", thiswot[0])
#    print('First Name: ', thiswot[1])
#    print('Last Name: ', thiswot[2])
#    print('Email: ', thiswot[3])
#    print('Job Title: ', thiswot[4])
#    print('Date Hired: ', thiswot[5])
#    print('Salary: ', thiswot[6])
#    print('__________________________________')











#___note____________________________________________________________

# i can do like this too

# 1. importing MySQL Connector package:
#import mysql.connector

# 2. Create Connection
#mydb = mysql.connector.connect (
#    host="localhost",
#   user='root',
#    passwd='Root'
  
#)

# 3. Creating an instance of a cursor
#mycursor = mydb.cursor()

# 4. choose database
#mycursor.execute('PyDB_Demo')
#__________________________________________________________________
