# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:53:41 2018

@author: james
"""

#before this code please cofigure sql server in your pc
#python -m pip install mysql-connector

#1.connect to database

import mysql.connector
mydb = mysql.connector.connect(host="127.0.0.1", user='root',database='mydatabase')
"""
Python MySQL
Python can be used in database applications.

One of the most popular databases is MySQL.

MySQL Database
To be able experiment with the code examples in this tutorial, you should have MySQL installed on your computer.

You can download a free MySQL database at https://www.mysql.com/downloads/.

Install MySQL Driver
Python needs a MySQL driver to access the MySQL database.

In this tutorial we will use the driver "MySQL Connector".

We recommend that you use PIP to install "MySQL Connector".

PIP is most likely already installed in your Python environment.

Navigate your command line to the location of PIP, and type the following:

Download and install "MySQL Connector":

C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install mysql-connector
Now you have downloaded and installed a MySQL driver.

Test MySQL Connector
To test if the installation was successful, or if you already have "MySQL Connector" installed, create a Python page with the following content:

demo_mysql_test.py:
"""
import mysql.connector
#If the above code was executed with no errors, "MySQL Connector" is installed and ready to be used.
"""
Create Connection
Start by creating a connection to the database.

Use the username and password from your MySQL database:

demo_mysql_connection.py:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

print(mydb)
#Now you can start querying the database using SQL statements.



"""
2.
Python MySQL Create Database
Creating a Database
To create a database in MySQL, use the "CREATE DATABASE" statement:

Example
create a database named "mydatabase":
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
"""
If the above code was executed with no errors, you have successfully created a database.

Check if Database Exists
You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement:

Example
Return a list of your system's databases:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"

)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
"""
Or you can try to access the database when making the connection:

Example
Try connecting to the database "mydatabase":
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)
"""
If the database does not exist, you will get an error.




3.
Python MySQL Create Table
Creating a Table
To create a table in MySQL, use the "CREATE TABLE" statement.

Make sure you define the name of the database when you create the connection

Example
Create a table named "customers":
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
"""
If the above code was executed with no errors, you have now successfully created a table.

Check if Table Exists
You can check if a database exist by listing all tables in your database by using the "SHOW TABLES" statement:

Example
Return a list of your system's databases:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

"""
Primary Key
When creating a table, you should also create a column with a unique key for each record.

This can be done by defining a PRIMARY KEY.

We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each record. Starting at 1, and increased by one for each record.

Example
Create primary key when creating the table:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
"""
If the table already exists, use the ALTER TABLE keyword:

Example
Create primary key on an existing table:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")




"""
4.
Python MySQL Insert Into Table
Insert Into Table
To fill a table in MySQL, use the "INSERT INTO" statement.

Example
Insert a record in the "customers" table:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
"""
Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.

Insert Multiple Rows
To insert multiple rows into a table, use the executemany() method.

The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:

Example
Fill the "customers" table with data:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


"""
Get Inserted ID
You can get the id of the row you just inserted by asking the cursor object.

Note: If you insert more that one row, the id of the last inserted row is returned.

Example
Insert one row, and return the ID:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

"""
5.
Python MySQL Select From
Select From a Table
To select from a table in MySQL, use the "SELECT" statement:

Example
Select all records from the "customers" table, and display the result:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
"""
Note: We use the fetchall() method, which fetches all rows from the last executed statement.

Selecting Columns
To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s):

Example
Select only the name and address columns:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
"""
Using the fetchone() Method
If you are only interested in one row, you can use the fetchone() method.

The fetchone() method will return the first row of the result:

Example
Fetch only one row:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)

"""
6.
Python MySQL Where
Select With a Filter
When selecting records from a table, you can filter the selection by using the "WHERE" statement:

Example
Select record(s) where the address is "Park Lane 38": result:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
"""
Wildcard Characters
You can also select the records that starts, includes, or ends with a given letter or phrase.

Use the %  to represent wildcard characters:

Example
Select records where the address contains the word "way":
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
"""
Prevent SQL Injection
When query values are provided by the user, you should escape the values.

This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.

The mysql.connector module has methods to escape query values:

Example
Escape query values by using the placholder %s method:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)  
  
"""  
7.
Python MySQL Order By
Sort the Result
Use the ORDER BY statement to sort the result in ascending or descending order.

The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order, use the DESC keyword.

Example
Sort the result alphabetically by name: result:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
"""
ORDER BY DESC
Use the DESC keyword to sort the result in a descending order.

Example
Sort the result reverse alphabetically by name:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


"""
8.

Python MySQL Delete From By
Delete Record
You can delete records from an existing table by using the "DELETE FROM" statement:

Example
Delete any record where the address is "Mountain 21":
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
"""
Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.

Notice the WHERE clause in the DELETE syntax: The WHERE clause specifies which record(s)
 that should be deleted. If you omit the WHERE clause, all records will be deleted!  
 """
 
 
"""
9.
Python MySQL Drop Table
Delete a Table
You can delete an existing table by using the "DROP TABLE" statement:

Example
Delete the table "customers":
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)
"""
Drop Only if Exist
If the the table you want to delete is already deleted, or for any other reason does not exist, you can use the IF EXISTS keyword to avoid getting an error.

Example
Delete the table "customers" if it exists:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)



"""
10.
Python MySQL Update Table
Update Table
You can update existing records in a table by using the "UPDATE" statement:

Example
Overwrite the address column from "Valley 345" to "Canyoun 123":
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
"""
Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.

Notice the WHERE clause in the UPDATE syntax: The WHERE clause specifies which record or records that should be updated. If you omit the WHERE clause, all records will be updated!

Prevent SQL Injection
It is considered a good practice to escape the values of any query, also in update statements.

This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.

The mysql.connector module uses the placeholder %s to escape values in the delete statement:

Example
Escape values by using the placholder %s method:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")




"""
10.
Python MySQL Limit
Limit the Result
You can limit the number of records returned from the query, by using the "LIMIT" statement:

Example
Select the 5 first records in the "customers" table:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
"""
Start From Another Position
If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:

Example
Start from position 3, and return 5 records:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
    

  
"""
  11.
  Python MySQL Join
Join Two or More Tables
You can combine rows from two or more tables, based on a related column between them, by using a JOIN statement.

Consider you have a "users" table and a "products" table:

users
{ id: 1, name: 'John', fav: 154},
{ id: 2, name: 'Peter', fav: 154},
{ id: 3, name: 'Amy', fav: 155},
{ id: 4, name: 'Hannah', fav:},
{ id: 5, name: 'Michael', fav:}
products
{ id: 154, name: 'Chocolate Heaven' },
{ id: 155, name: 'Tasty Lemons' },
{ id: 156, name: 'Vanilla Dreams' }
These two tables can be combined by using users' fav field and products' id field.

Example
Join users and products to see the name of the users favorite product:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
#Note: You can use JOIN instead of INNER JOIN. They will both give you the same result.

"""
LEFT JOIN
In the example above, Hannah, and Michael were excluded from the result, that is because INNER JOIN only shows the records where there is a match.

If you want to show all users, even if they do not have a favorite product, use the LEFT JOIN statement:

Example
Select all users and their favorite product:
"""
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"

"""
RIGHT JOIN
If you want to return all products, and the users who have them as their favorite, even if no user have them as their favorite, use the RIGHT JOIN statement:

Example
Select all products, and the user(s) who have them as their favorite:
"""
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"