# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:55:09 2018

@author: sky
"""


#open a file
fo = open(r"new.txt", "w+")


x=open("new.txt",'r')
"""
Modes
r	
reading only
file pointer is placed at the beginning of the file.


r+	
Opens a file for both reading and writing.
not overwrite 
The file pointer placed at the beginning of the file.

	
w
Opens a file for writing only. 
Overwrites the file if the file exists. 
If the file does not exist, creates a new file for writing.

W+
Opens a file for both writing and reading. 
Overwrites the existing file if the file exists. 
If the file does not exist, creates a new file for reading and writing.


a	
Opens a file for appending. 
The file pointer is at the end of the file if the file exists. 
That is, the file is in the append mode. 
If the file does not exist, it creates a new file for writing.

a+	
Opens a file for both appending and reading. 
The file pointer is at the end of the file if the file exists. 
The file opens in the append mode. If the file does not exist, 
it creates a new file for reading and writing.

      pointer location  Mode
r          start         r

r+         start         r/w

w          start         w

w+         start         r/w

a           end          a

a+          end          a/r
"""




"""
Attribute
flie.close
file.closed
file.mode
file.name
file.tell()# current position
file.seek(0,0)# change the pointer location
"""

file=open(r'new.txt','a+'), 
 #write data in file
file.write('Hello World')
#after write emidiate read not works because pointer at last position
strr=file.read()
#file closing
file.close()

#with keyword
with open(r'new.txt','r') as file:
    strr=file.read()
    
file.closed
file.mode

#read after writing
file=open(r'new.txt','r+') 
file.write('Hello World')
file.seek(0,0)
strr=file.read()
file.close()

#check file name
print( "Name of the file: ", file.name)
#check weather file is closed or not
print ("Closed or not : ", file.closed)
#check open mode
print ("Opening mode : ", file.mode)


#reposition pointer with seek
file = open(r'E:\new.txt','r+') 
file.write('Hello World')
strr=file.read()
print(strr)
position = file.seek(0);
strr=file.read()
print(strr)

#append mode
file= open('testfile.txt','a') 
file.write('Hello World')
strr=file.read()
print(strr)
file.close()

#r+ mode
file = open('testfile.txt','r+')  
file.write('Hello World')
strr=file.read()
print(strr)
file.close()

#a+ mode
file = open(r'E:\new.txt','a+')  
file.write('asdfg')
position = file.seek(0, 0);
strr=file.read()
print(strr)
file.close()

#r+ mode
file = open('testfile.txt','r+')  
file.write('Hello World')
strr=file.read()
print(strr)



# Check current position
position = file.tell();
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = file.seek(0, 0);
#read first ten char
str2 = file.read(10);
print ("Again read String is : ", str)
# Close opend file
file.close()


#with keyword
with open('new.txt','r') as fo:
   fo.write()
   fo.read()
 
    
file = open(r'new.txt','a+') 
file.write('abc\nbhu')
file.close() 

#read line by line
file = open(r'new.txt','r') 
for i in file.readlines():
    print(i)
    
#copy data one file to other
f1=open(r'New.txt','r+')
x=f1.readlines()
f1.close()
f2=open(r'new2.txt','a+')
x3=[]
for i in x:
    x2=''
    for j in i:
        
        f2.write(j)
f2.close()









