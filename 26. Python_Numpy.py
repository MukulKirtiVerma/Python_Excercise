# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 13:14:34 2018

@author: Mukul Kirti Verma
"""
#Numpy lib is beautiful library for mathmatical  operations .

# to install numpy
!pip install numpy

#import numpy
import numpy as np 
#convert list to array=========
a = np.array([1, 2, 3, 4]) 
#create multi dim array===========
a = np.array([[1, 2], [3,4],[5,6]])

#define data type or array=========
x = [1,2,3] 
a = np.asarray(x, dtype = float) 
print( a )
a = np.asarray(x, dtype = str) 

#tuple to array
x = (1,2,3) 
a = np.asarray(x) 




#check the shape of array==========
a = np.array([[1,2,3],[4,5,6]]) 
print (a.shape) 

#change the shape of array=========
a.shape=(1,6)
print( a )

#create sequential array===============
#np.arange(start,end,linsoace)
#default start=0 and linspac =1
a = np.arange(5) 
print( a )
a = np.arange(1,8,1) 
print( a )

#reshape array========================
a = np.arange(24) 
b=a.reshape(12,2) 
print (b)

#itemsize gives the total byte for each element in array
x = np.array([1,2,3,4,5], dtype = np.int32) 
print (x.itemsize)

#create a array of zeros=======================
x = np.zeros(6) 
print (x)

#create array of ones=========================
x = np.ones(5) 
print (x)

#create array of equal distribution===========
#np.linspace(start,end,linspace) 
x = np.linspace(10,20,5) 
print(x)

#endpoint = False then end will not include in array========
x = np.linspace(10,20, 5, endpoint = False)
print( x )

#retstep = True show the diffrence b/w array=================
x = np.linspace(1,10,4, retstep = True) 
print (x)

#log of element of array with equal space===================
a = np.logspace(1,10,num = 10, base = 2) 
print (a)

#access element of array 1 dimention
a = np.arange(10) 
b = a[4] 
print (b)


#acces element in 2d========================
#syntax arr[start row : end row : increment by , start col : end col : increment by]
a = np.arange(10) 
a.shape=(5,2)
print (a)

#print 1st col==========================
b = a[:,1:2] 
print (b)


#print 1st row==========================
b = a[1:2,:] 
print (b)

#from 1st row print all====================
b = a[1:,:] 
print (b)


#from 1st col print all=====================
b = a[:,1:] 
print (b)

#increment slice by 2======================
a = np.arange(10) 
b = a[2:7:2]
print(b)

#row only slice=============================
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
a[0:2]
print( a[1:])
#a[row,col]

# slice single row or col=====================
#slice single col=============================
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print( a[...,2])


#slice row only==============================
a = np.array([[1,2,3,1],[3,4,5,1],[4,5,6,1]]) 

print( a[2,...])

#slice both=====================================
a = np.array([[1,2,3,1],[3,4,5,1],[4,5,6,1]]) 

print( a[1:3,2:4])
 
a = np.arange(10) 
b = a[2:7:3] 


a = np.arange(6) 
print (a[:5:1])




#create run time array by user define input===========
r=int(input())#enter row's
c=int(input())#enter cols
a=np.zeros(r*c)#create array or zeros=================
for i in range(r*c):
    a[i]=int(input("enter no."))#input array element=====
a.shape=(r,c)


# or create list of user input and convert to array===========

a = list(np.array([[1,2,3],[3,4,5],[4,5,6]]))
print (a[0])
a[0]=[7,8,9]
print (a[1:2])
print (a[1,1])



l=[]
x=int(input())
y=int(input())
for i in range(0,x):
    l1=[]
    for j in range(0,y):
        l1.append(int(input()))
    l.append(l1)
 
#transpose=========================================
    
import numpy as np
    
i=int(input())
j=int(input())
a=np.zeros(i*j)
a.shape=(i,j)
for ii in range (i):
    for jj in range(j):
        a[ii][jj]=int(input())



a.shape=(1,i*j);
k=0;
b=np.zeros(i*j)
b.shape=(j,i)
for ii in range(i):
    for jj in range(j):
        b[jj][ii]=a[0][k]
        k=k+1
        



#Trans==============================================        
i=int(input())
j=int(input())
a=np.zeros(i*j)
a.shape=(i,j)        
        
#eg     
l2=[]
b=np.zeros(i*j)
b.shape=(j,i)
for k in range(0,i):
    for kk in range(0,j):
        a[k][kk]=int(input())
        
 #eg       
for k in range(0,i):
    for kk in range(0,j):
        if(k==kk):
            l2.append(a[k][kk])
        if(k+kk==i-1):
            if(k!=kk):
                l2.append(a[k][kk])
       
"""        
Some numpy operations        

1. Elementwise operations
2. Basic operations
3. With scalars:
"""
import numpy as np
a = np.array([1, 2, 3, 4])
b=a + 1


#All arithmetic operates elementwise====================

b = np.ones(4) + 1
print(b)
#====================================
c=a - b
print(c)
#====================================
d=a * b
print(d)
#======================================
j = np.arange(5)
2**(j + 1) - j

#These operations are of course much faster than if you did them in pure python:


a = np.arange(10000)
a + 1  
#or
l = range(10000)
[i+1 for i in l] 


# Array multiplication is not matrix multiplication:========
c = np.ones((3, 3))
d=c * c    
print(d)               # NOT matrix multiplication!


# Matrix multiplication:
d=c.dot(c)
print(d)

"""
#Elementwise operations

Try simple arithmetic elementwise operations: add even elements with odd elements
Time them against their pure python counterparts using %timeit.
Generate:
"""
    
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
a == b

print(a > b)
"""
Array-wise comparisons: >>>>>> a = np.array([1, 2,...
Logical operations:
"""

a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)
print(np.logical_or(a, b))
#====================================

print(np.logical_and(a, b))
#====================================

print(np.logical_xor(a, b))




#Transcendental functions:=======================


a = np.arange(5)
#sin===============================================
print(np.sin(a))
#log===============================================
print(np.log(a))
#e pow x ===========================================
print(np.exp(a))


#Shape mismatches===================================

a = np.arange(4)
a + np.array([1, 2])  


#Broadcasting? ===============================


#create triangular matrix============================
a = np.triu(np.ones((3, 3)), 1)   # see help(np.triu)
print(a)
#transpose==========================================
print(a.T)


"""
The transposition is a view
As a results, the following code is wrong and will not make a matrix symmetric:
"""

a += a.T
print(a)



#sum func==========================================
x = np.array([1, 2, 3, 4])
print(x.sum())


x = np.array([[1, 1], [2, 2]])
print(x.sum())


print(x.sum(axis=0) )  # columns sum (first dimension)
#col 0 and col 1  indivisual sum===============================
print(x[:, 0].sum(), x[:, 1].sum())

#row wise sum==================================================
print(x.sum(axis=1))  # rows (second dimension)

print(x[0, :].sum(), x[1, :].sum())




#some oter func
x = np.array([1, 3, 2])
#min of array======================
print(x.min())
#max of array=====================
print(x.max())


print(x.argmin())  # index of minimum

print(x.argmax())  # index of maximum

#===============================================
#Logical operations:

#check all are True or not
print(np.all([True, True, False]))
#check any is True or not
print(np.any([True, True, False]))

#Note Can be used for array comparisons:
#!= operator============================
a = np.zeros((100, 100))
print(np.any(a != 0))
#== operator
print(np.all(a == a))

#<= and >= operator
a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])
print(np.all(((a <= b) & (b <= c))))

 

# mean median,mode ,std
x = np.array([1, 2, 3, 1])
y = np.array([[1, 2, 3], [5, 6, 1]])
print(x.mean())
print(np.median(x))
print(x.std())         # full population standard dev.


#eg
k=[]
for i in range(1,6):
    l=[]
    for j in range(1,11):
        l.append(i*j)
    k.append(l)
import numpy as np
x=np.asarray(k)
h=int(input())
x=x.T
print(x[...,h])


