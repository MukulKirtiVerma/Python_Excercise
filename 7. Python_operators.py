# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 12:44:07 2018

@author: sky
"""

#!/usr/bin/python

"""
Python has 7 type of operator let see one by one"""
"""
1. Arithmatic Operator


+ plus
- substract
* mul
/ div
%  modulo
**  power
//  floor operator
"""

##first define all data type and the we will see how operator work on 
#diffrent data types
i=2
j=3
print(i+j)
print(i-j)
print(i*j)
print(i/j)
print(i%j)
print(i**j)
print(i//j)

i=2.0
j=3.5
print(i+j)
print(i-j)
print(i*j)
print(i/j)
print(i%j)
print(i**j)
print(i//j)

i=2+3J
j=5+1j
print(i+j)
print(i-j)
print(i*j)
print(i/j)
print(i%j)
print(i**j)
print(i//j)

i="abc"
j="def"
print(i+j)
print(i-j)
print(i*j)
print(i/j)
print(i%j)
print(i**j)
print(i//j)

i=True
j=False
print(i+j)
print(i-j)
print(i*j)
print(i/j)
print(i%j)
print(i**j)
print(i//j)

"""
2. Comparison Operator:
==   equal equal
!=   Not equal
<>   Not equal in python 2.x
>    greter then
<    less then
>=   greater then or equal to
<=   less then or equal to
"""

i=2
j=3
print(i==j)
print(i!=j)
print(i>j)
print(i<j)
print(i>=j)
print(i<=j)
#print(i<>j) in python 2.x 

i=2.0
j=3.5
print(i==j)
print(i!=j)
print(i>j)
print(i<j)
print(i>=j)
print(i<=j)
#print(i<>j)

i=2+3J
j=2+3j
print(i==j)
print(i!=j)
print(i>j)
print(i<j)
print(i>=j)
print(i<=j)
#print(i<>j)

i="abc"
j="hgi"
print(i==j)
print(i!=j)
print(i>j)
print(i<j)
print(i>=j)
print(i<=j)
#print(i<>j)

i=True
j=False
print(i==j)
print(i!=j)
print(i>j)
print(i<j)
print(i>=j)
print(i<=j)
#print(i<>j)


"""
3. Assignment Operator
=    Assign
+=   add then assign
-=   Substract then assign
*=   Mul the assign
/=   Div then Assign
%=   Modulo then assign
**=  Pow then Assign
//=  Floor Div then Assign
"""

i=2
j=3
i=i+j
print(i)
i+=j    #i=i+j
print(i)
i-=j 
print(i)
i*=j
print(i)
i/=j
print(i)
i%=j
print(i) 
i**=j     #i=i**j
print(i)
i//=j   #i=i//j
print(i)

i=2.0
j=3.5
i=i+j
print(i)
i+=j    #i=i+j
print(i)
i-=j 
print(i)
i*=j
print(i)
i/=j
print(i)
i%=j
print(i) 
i**=j     #i=i**j
print(i)
i//=j   #i=i//j
print(i)

i=2+3J
j=2+3j
i=i+j
print(i)
i+=j    #i=i+j
print(i)
i-=j 
print(i)
i*=j
print(i)
i/=j
print(i)
i%=j
print(i) 
i**=j     #i=i**j
print(i)
i//=j   #i=i//j
print(i)

i="abc"
j="hgi"
i=i+j
print(i)
i+=j    #i=i+j
print(i)
i-=j 
print(i)
i*=j
print(i)
i/=j
print(i)
i%=j
print(i) 
i**=j     #i=i**j
print(i)
i//=j   #i=i//j
print(i)

i=True
j=False
i=i+j
print(i)
i+=j    #i=i+j
print(i)
i-=j 
print(i)
i*=j
print(i)
i/=j
print(i)
i%=j
print(i) 
i**=j     #i=i**j
print(i)
i//=j   #i=i//j
print(i)


"""
4. Bitwise operator

&  AND
|  OR
^  XOR
~  NOT
>> RIGHT SHIFT
<< LEFT SHIFT



             &           |         ^
i=2 0010   0010(2)    0011(3)   0001(1)
j=3 0011
  
  
  
XOR
A XOR B = A' B + A B'
A OR B = A+B
A AND B = A.B 

A  B   XOR   OR    AND
0  0    0     0     0
0  1    1     1     0
1  0    1     1     0
1  1    0     1     1
"""


i="hi"
j="ki"
print(i&j)
print(i|j)
print(i^j)
print(~i)
print(i>>2)
print(i<<2)

i=True
j=False
print(i&j)
print(i|j)
print(i^j)
print(~i)
print(i>>2)
print(i<<2)

j=2.0
i=3.1
print(i&j)
print(i|j)
print(i^j)
print(~i)
print(i>>2)
print(i<<2)

i=2+3j
j=2+5j
print(i&j)
print(i|j)
print(i^j)
print(~i)
print(i>>2)
print(i<<2)

i=1               
j=3
print(i&j)
print(i|j)
print(i^j)
print(~i)
print(i>>2)
print(i<<2)


"""
5. logical operator
and
or
not

and
T T  T
T F  F
F T  F
F F  F

or
T T T
T F T
F T T
F F F

not

T F
F T
"""

i=2
j=3
k=8
print(i<=j and k>=j and k>j)
print(i<j or i>j)
print(not i>j)

i="hi"
j="ki"
print(i<=j and k>=j and k>j)
print(i<j or i>j)
print(not i>j)

i=True
j=False

print(i<=j and k>=j and k>j)
print(i<j or i>j)
print(not i>j)

"""
6. Membership Operator
in  -  it check the membership of object in a iterable object, if found the return True else False
not in - if object found in iterable object then return False else True  

"""

#================================
print(2 in (1,2,3,5,6))
#==================================
print(2+5j in [1,2,3,4,5,2+5j])
#==================================

'Hello' in 'Hello world!'
#==================================================
'hello' in 'Hello world!' #check case sensitevity
#===================================================
'house' in 'Hello world!'
#=================================================
'hello' in 'Hello world!'
#=================================================
'orld' in 'Hello world!'   #match when word slice occure in iterable object
#==================================================
'Hello' not in 'Hello world!'
#============================================================
'car' not in 'Hello world!'
#==================================================
'house' not in 'Hello world!'
#====================================================


"""
7. Identity Oerator
is      - if two or more reference pointer pointing to same object the return True else False
not is  - If two or more Referance pointer pointing to diffrent object the return True otherwise False
"""
a = 20
b = 20
if ( a is not b ):
   print("Line 1 - a and b have same identity")
else:
   print ("Line 1 - a and b do not have same identity")
#=====================================================
if ( id(a) == id(b) ):
   print ("Line 2 - a and b have same identity")
else:
   print("Line 2 - a and b do not have same identity")
#======================================================
b = 30
if ( a is b ):
   print("Line 3 - a and b have same identity")
else:
   print("Line 3 - a and b do not have same identity")
#=========================================================
if ( a is not b ):
   print ("Line 4 - a and b do not have same identity")
else:
   print ("Line 4 - a and b have same identity")
   
#===========================================================


"""
EXAMPLES
"""

x = True
y = False

# Output: x and y is False
print('x and y is',x and y)

# Output: x or y is True
print('x or y is',x or y)

# Output: not x is False
print('not x is',not x)




for x in range(11, 1):
    for y in range(11, 1):
        print ((x, y, x*y))
        
        
string = "Hello World"
for x in string:
    print( x)

for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print ('Current Letter :', letter)
  
var = 10                    # Second Example
while var > 0:              
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
      break

print ("Good bye!")




for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print( "Good bye!")


for letter in 'Python': 
   if letter == 'h':
       print ('Current Letter :', letter)

print ("Good bye!")



#in operator
for i,j in range(10):
  print(i)
for i in range(1,10):
  print(i)
for i in range(1,10,2):
  print(i)
for i in range(10,1,-2):
  print(i)
  

  
for i, c in enumerate('test'):
    print( i, c)
  
  
for i, j in zip(range(10), range(5,18,2)):
    print(i,j)
  
    
for i in (('hiiiii',2)):
    print(i)
    
for i, c in enumerate('kkkkkk'):
    print( i, c)
    
for i, c in enumerate('kkkkkk',start=2):
    print( i, c) 
    
for i, c in enumerate('kkkkkk',start=2, end=5):
    print( i, c)
    
    
    
string="hjkkjkjk"    
for c in string[0:3]:
    print(c)
    
    
    
for i in range(0,5):
    for j in range(0,i):
        print(i)
    if(i==5):
        break