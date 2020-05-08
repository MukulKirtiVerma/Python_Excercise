# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 22:27:47 2018

@author: james
"""
#before run this file please run mongodb server
#check weather mongodb server running or not by url https://localhost:27017/

import pymongo
"""
Creating a Database

To create a database in MongoDB, 
start by creating a MongoClient object, 
then specify a connection URL with 
the correct ip address and the name of the
 database you want to create.

MongoDB will create the database if it 
does not exist, and make a connection to it.
"""


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]


#Check if "mydatabase" exists:
    
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
  
  
#Create a collection called "customers":
    
mycol = mydb["customers"]


"""
Check if Collection Exists
Remember: In MongoDB, a collection is not 
created until it
 gets content, so if this is your first 
 time creating a collection, 
 
 (create document) before you check if 
 the collection exists!

You can check if a collection exist in a database by 
listing all collections:
Return a list of all collections in your database:
"""
    
print(mydb.list_collection_names()) 


"""
You can check if a database exist by listing 
all databases in you system:

Return a list of your system's databases:
"""
print(myclient.list_database_names())



#Check if the "customers" collection exists:

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
   
  
  
  
  
#Insert a record in the "customers" collection:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)  



"""
Return the _id Field
The insert_one() method returns a InsertOneResult object, 
which has a property, inserted_id, that holds the 
id of the inserted document.

Example
Insert another record in the "customers" collection, 
and return the value of the _id field:
"""
mydict = { "name": "Peter", "address": "Lowstreet 27" }

x = mycol.insert_one(mydict)

print(x.inserted_id)



"""
Insert Multiple Documents
To insert multiple documents into a collection in 
MongoDB, we use the insert_many() method.

The first parameter of the insert_many() method is a 
list containing dictionaries with the data you want to insert:

"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)



"""
Find One
To select data from a collection in MongoDB, 
we can use the find_one() method.

The find_one() method returns the first 
occurrence in the selection.

Example
Find the first document in the customers collection:
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.find_one()

print(x)




"""
Find All
To select data from a table in MongoDB, 
we can also use the find() method.

The find() method returns all occurrences in the selection.

The first parameter of the find() method is a query object.
No parameters in the find() method gives you the same 
result as SELECT * in MySQL.

Example
Return all documents in the "customers" 
collection, and print each document:
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find():
  print(x)
  
  
""" 
  
Return Only Some Fields
The second parameter of the find() method 
is an object describing which fields to include in the result.

This parameter is optional, and if omitted, 
all fields will be included in the result.

Example
Return only the names and addresses, not the _ids:
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find({},{ "_id": 1, "name": 1, "address": 1 }):
  print(x)




"""
You are not allowed to specify both 0 and 1 values in the same 
object (except if one of the fields is the _id field). If you 
specify a field with the value 0, all other fields 
get the value 1, and vice versa:

Example
This example will exclude "address" from the result:
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find({},{ "address": 0 }):
  print(x)
  
  
  
  
""" 
Python MongoDB Query
Filter the Result
When finding documents in a collection, 
you can filter the result by using a query object.

The first argument of the find() method is a 
query object, and is used to limit the search.

Example
Find document(s) with the address "Park Lane 38":
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)


"""

Advanced Query
To make advanced queries you can use modifiers 
as values in the query object.

E.g. to find the documents where the "address" 
field starts with the letter "S" or higher 
(alphabetically), use the greater than modifier: {"$gt": "S"}:

Example
Find documents where the address starts 
with the letter "S" or higher:
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$gt": "S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
  
  
  
"""
Filter With Regular Expressions
You can also use regular expressions as a modifier.

Regular expressions can only be used to query strings.

To find only the documents where the "address" 
field starts with the letter "S", use the regular 
expression {"$regex": "^S"}:

Example
Find documents where the address starts with the letter "S":
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)  
  
  
  
  
"""  
Python MongoDB Sort
Sort the Result
Use the sort() method to sort the result in ascending 
or descending order.

The sort() method takes one parameter for 
"fieldname" and one parameter for "direction" 
(ascending is the default direction).

Example
Sort the result alphabetically by name:
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)
  
  
"""
Sort Descending
Use the value -1 as the second parameter to sort descending.
"""
sort("name", 1) #ascending
sort("name", -1) #descending
"""
Example
Sort the result reverse alphabetically by name:
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name", -1)

for x in mydoc:
  print(x)
  
  
 
"""
Python MongoDB Delete Document
Delete Document
To delete one document, we use the delete_one() method.

The first parameter of the delete_one() method is 
a query object defining which document to delete.

Note: If the query finds more than one document, 
only the first occurrence is deleted.

Example
Delete the document with the address "Mountain 21":
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)




"""
Delete Many Documents
To delete more than one document, use the delete_many() method.

The first parameter of the delete_many() 
method is a query object defining which documents to delete.

Example
Delete all documents were the address starts with the letter S:
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")





"""
Delete All Documents in a Collection
To delete all documents in a collection, 
pass an empty query object to the delete_many() method:

Example
Delete all documents in the "customers" collection:
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")    


"""
Python MongoDB Drop Collection
Delete Collection
You can delete a table, or collection as it 
is called in MongoDB, by using the drop() method.

Example
Delete the "customers" collection:
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mycol.drop()

"""
The drop() method returns true if the collection was dropped 
successfully, and false if the collection does not exist.
"""

"""
Python MongoDB Update

Update Collection
You can update a record, or document as 
it is called in MongoDB, by using the update_one() method.

The first parameter of the update_one() 
method is a query object defining which document to update.

Note: If the query finds more than one 
record, only the first occurrence is updated.

The second parameter is an object defining 
the new values of the document.

Example
Change the address from "Valley 345" to "Canyon 123":
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

x=mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)
  
  
"""  
Update Many
To update all documents that meets the 
criteria of the query, use the update_many() method.

Example
Update all documents where the address 
starts with the letter "S":
"""
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")



#Python MongoDB Limit(5 times)
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x)
  
  
#https://www.mongodb.org/dl/win32/i386
