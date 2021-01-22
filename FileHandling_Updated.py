# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:57:46 2021

@author: Mukul Kirti Verma
"""

file=open('myfile.txt','w')
'buffer',
 'close',
 'closed',
 'detach',
 'encoding',
 'errors',
 'fileno',
 'flush',
 'isatty',
 'line_buffering',
 'mode',
 'name',
 'newlines',
 'read',
 'readable',
 'readline',
 'readlines',
 'reconfigure',
 'seek',
 'seekable',
 'tell',
 'truncate',
 'writable',
 'write',
 'write_through',
 'writelines'
 

The Python file detach() method is used to separate 
the underlying raw stream from the buffer and return it. 
After the raw stream has been detached, the buffer is in an unusable state.

Some buffers, like BytesIO, do not have the concept of a 
single raw stream to return from this method. 
They raise UnsupportedOperation.



file=open('myfile.txt','w')
file.detach()
file.write('hello')


file=open('myfile.txt','w')
file.error()
file.write('hello')


Delete a File
import os
os.remove("python_test.txt") 



Check if File exist
To check whether a file exists or not, the os module contains path.exists() function which can be used to check it.

import os
if os.path.exists("python_test.txt"):
  os.remove("python_test.txt")
else:
  print("The file does not exist")
  
  
  
  
Delete Folder
The os module contains rmdir() function which can be used to delete an entire folder.

import os
os.rmdir("myfolder")



The Python file detach() method is used to separate
 the underlying raw stream from the buffer and return it. 
 After the raw stream has been detached, the buffer is in an unusable state.

Some buffers, like BytesIO, do not have the concept of a single 
raw stream to return from this method. They raise UnsupportedOperation.

file=open('myfile.txt','w')
file.detach()
file.write('hello')



Return Value
Returns the file descriptor of the file stream as a number.

Example: Close an opened file in Python
In the below example, Python fileno() method is used 
to return the file descriptor of the file stream of file called MyFile.

MyFile = open("python_test.txt", "w")
MyFile2 = open("python_test.txt", "w")

#file descriptor of the file stream
x = MyFile.fileno()
print(x)
MyFile.close()
MyFile2.close()


Flush

MyFile = open("python_test.txt", "w+")
MyFile.write('hello')
MyFile.close()
#read content before closing the file
MyFile = open("python_test.txt", "r")

print(MyFile.read())
#flushing the internal buffer
MyFile.flush()
print(MyFile.read())

#closing the open file
MyFile.close()



Readable
MyFile = open("python_test.txt",'w')
print(MyFile.readable())


Truncate
MyFile = open("python_test.txt", "a")

#Assuming the file contains
#This is line 1 content.
#This is line 2 content.
#This is line 3 content.

#file is truncated to 30 byte size
MyFile.truncate(30)
MyFile.close()

#content of the file after truncate
MyFile = open("python_test.txt", "r")
print(MyFile.read())
MyFile.close()


Seekable
MyFile = open("python_test.txt", "r")

print(MyFile.seekable())


Writelines
MyFile = open("python_test.txt", "a")
#list iterable is used here
MyFile.writelines(["Add more content.", "Add this content also."])
MyFile.close()

#overwrite existing content of the file 
MyFile = open("python_test.txt", "x")
#tuple iterable is used here
MyFile.writelines(["Add more content.", "Add this content also."])
MyFile.close()