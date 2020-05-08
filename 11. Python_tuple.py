# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:57:15 2018

@author: sky
"""
"""
A tuple is a sequence of immutable Python objects.
 Tuples are sequences, just like lists. The main difference between the tuples and the lists is that the tuples cannot be changed unlike lists. Tuples use parentheses, whereas lists use square brackets.
Creating a tuple is as simple as putting different comma-separated 
values. Optionally, you can put these comma-separated values between parentheses also. For example −
"""
#create tuple
#empty tuple
tup1 = ()
#tuple with single element
tup1 = (50,)
#multielement
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
#another way to create tuple
tup3 = "a", "b", "c", "d"

#The empty tuple is written as two parentheses containing nothing −

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print ("tup1[0]: ", tup1[0]);
print ("tup2[1:5]: ", tup1[1:5]);




#Updating Tuples===================================================
#all these line will give error because tuple cannot be change
tup1[1]=  "physics"

del tup1[0]
del tup1[8:9]


#
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');


#tuple concatination==============================================
tup1 = tup1 + tup2;
print (tup1);

#create tuple by user input=======================================
tup1=()
for i in range(1,6):
    x=input("enter element")
    j=(x,)
    tup1=tup1+j


#Access Tuple Elements============================================
print(tup1[0])
print(tup1[0:5])

#some methods=====================================================

#length 

len(tup)

#concatination

(1, 2, 3) + (4, 5, 6)
#repetition

('Hi!',) * 4

#membership

3 in (1, 2, 3)


#Iteration

for x in (1, 2, 3): 
    print(x)


len((2,3,4))


"""++++++++++++++++"""
L = ('Spam', 'SPAM!',"spam")
#max
max(L)

#min
min(L)
"""
order of sorting
0
9
A
Z
a
z
"""

#typecasting======================================================
t=2
print(tuple(t))#error

t=2.3
print(tuple(t))#error

t="abc"
print(tuple(t))

t=2+3j
print(tuple(t))#error

t=True
print(tuple(t))#error

t=[1,2,3]
print(tuple(t))

t={1:2,2:3,4:5}
print(tuple(t))


#============================================================
L = ('Spam', 'SPAM!',"spam")
#count method
L.count("spam")
#index
L.index("spam")

#some examples===============================================
tup1=()
for i in range(0,5):
    j=input()
    tup2=((j),)
    tup1=tup1+tup2
print(tup1)

tup1=tuple(True)

#=======================================================
l1=[]
l=[]
for i in range(0,3):
    l1.append(l)
    for j in  range(0,3):
        l.append(input())
    l=[]
print(l)
        
        
        
        