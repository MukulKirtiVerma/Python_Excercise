# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:07:45 2020

@author: Mukul Kirti Verma
"""

"""=================================================================
Variables are nothing but reserved memory locations to store values.
 It means that when you create a variable, you reserve some space 
 in the memory.

Based on the data type of a variable, the interpreter allocates 
memory and decides what can be stored in the reserved memory. 
Therefore, by assigning different data types to the variables, 
you can store integers, decimals or characters in these variables.

Assigning Values to Variables
Python variables do not need explicit declaration to reserve memory
space. The declaration happens automatically when you assign a value to a variable.
The equal sign (=) is used to assign values to variables.

The operand to the left of the = operator is the name of the
variable and the operand to the right of the = operator is the 
value stored in the variable. For example −
"""

counter=100  #an integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print (counter)
print (miles)
print (name)

"""===========================================================
Python has five standard data types −
1. Numbers
2. String
3. List
4. Tuple
5. Dictionary

"""

"""
1. Python Numbers
Number data types store numeric values. Number objects are created when you assign a value to them. For example −
"""
var1 = 1
var2 = 10

#You can also delete the reference to a number object by using 
#the del statement. The syntax of the del statement is −

#del var1[,var2[,var3[....,varN]]]]
del var
del var1, var2


"""
Python supports three different numerical types −

a. int (signed integers)
b. float (floating point real values)
c. complex (complex numbers)
All integers in Python3 are represented as long integers. Hence, there is no separate number type as long.
"""

"""
Here are some examples of numbers −

int  	float	   complex
10	     0.0	    3.14j
100	    15.20	    45.j
-786	-21.9	    9.322e-36j
080	   32.3+e18	    .876j
-0490	 -90.    	-.6545+0J
-0x260	-32.54e100 	3e+26J
0x69	70.2-E12	4.53e-7j
"""


"""============================================================
2. String
Strings in Python are identified as a contiguous set of characters represented in the quotation marks. 
Python allows either pair of single or double quotes.
The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator. For example −
"""


str1="hi how are you."
str2="fine thank you"
print(str1)   
print(str1[0])#access string single char
print(str1+str2)


"""
3. Python Lists=================================================
Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]). To some extent, lists are similar to arrays in C. One of the differences between them is that all the items belonging to a list can be of different data type.

The values stored in a list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1. The plus (+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator. For example −
"""

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists


"""=============================================================
4. Python Tuples
A tuple is another sequence data type that is similar to the 
list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parenthesis.

The main difference between lists and tuples are − Lists are 
enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists. For example −
"""

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           # Prints complete tuple
print (tuple[0])        # Prints first element of the tuple
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple


"""
5. Python Dictionary============================================
Python's dictionaries are kind of hash-table type. 
They work like associative arrays or hashes found in 
Perl and consist of key-value pairs. A dictionary key 
can be almost any Python type, but are usually numbers or 
strings. Values, on the other hand, can be any arbitrary 
Python object.

Dictionaries are enclosed by curly braces ({ }) and 
values can be assigned and accessed using square braces ([]).
Example:-
"""

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values
