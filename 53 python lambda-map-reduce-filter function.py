# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:18:56 2020

@author: MUKUL
"""


    

x = lambda a : a + 10
print(x(5))


x = lambda a, b : a * b
print(x(5, 6))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))



x = lambda a, b, c : a + b + c
print(x(5, 6, 2))




def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(3)

print(mydoubler(11))



def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))



def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

def fun (x):
    return x*x
l=[1,2,3]
print(list(map(fun,l)))

map(fun, iter)



def addition(n): 
    return n + n 
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 


numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 
number3  = [7, 8, 9]
result = map(lambda x, \
             y, z: x + y + z,\
             numbers1, \
             numbers2,\
             number3) 
print(list(result))


  
numbers = (1, 2, 3, 4) 
result = map(lambda x: x + x, \
             numbers) 
print(list(result)) 



l = ['sat', 'bat', 'cat', 'mat'] 
  
# map() can listify the list of strings individually 
test = list(map(list, l)) 
print(test) 

reduce() in Python


reduce() in Python

def fun (x):
    return x
l=[1,2,3,4,5]




import functools 
  
# initializing list 
lis = [ 1 , 3, 5, 6, 2, ] 
  
# using reduce to compute sum of list 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda\
                        a,b : \
                        a+b,\
                        lis)) 
  
# using reduce to compute maximum element from list 
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(\
 lambda a,b : a if a > b else b,lis)) 
count=[0]
print (functools.reduce(\
 lambda a,b : count.(count[0]+1) if b % 2!=0 else count,lis)) 

def fun(x,y):
    if(y%2!=0):
        count[0]=count[0]+1
        return count
    else:
        return count
functools.reduce(\
            lambda x,y\
            :x+1 \
            if y%2!=0 \
            else x, [0]+lis)
print(count[0])

lis=[0]
def fun(x,y):
    print(x,y)
    if(y%2!=0):
        return x+1
    else:
        return x
lis=[9,2,1,3,5,7,9,8]
functools.reduce(fun, [0]+lis)

    
g=
import functools 
  
# importing operator for operator functions 
import operator 
  
# initializing list 
lis = [ 1 , 3, 5, 6, 2, ] 
  
# using reduce to compute sum of list 
# using operator functions 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(\
        operator.add,lis)) 
  
# using reduce to compute product 
# using operator functions 
print ("The product of list elements is : ",end="") 
print (functools.reduce(operator.mul,lis)) 
  
# using reduce to concatenate string 
print ("The concatenated product is : ",end="") 
print (functools.reduce(operator.add,["hi","hello","by"])) 



import itertools 
  
# importing functools for reduce() 
import functools 
i
# initializing list  
lis = [ 1, 3, 4, 10, 4 ] 
  
# priting summation using accumulate() 
print ("The summation of list using accumulate is :",end="") 
print (list(itertools.accumulate(lis,lambda x,y : x+y))) 
  
# priting summation using reduce() 
print ("The summation of list using reduce is :",end="") 
print (functools.reduce(lambda x,y:x+y,lis)) 



filter() in python
Last Updated: 22-04-2020
#The filter() method filters 
the given sequence with the help of a function 
that tests each element in the 
sequence to be true or not.


def fun(variable): 
  letters = ['a', 'e',\
             'i', 'o', 'u'] 
  if (variable in letters): 
        return True
  else: 
        return False
# sequence 
sequence = ['g', 'e', \
            'e', 'j', \
            'k', 's', \
            'p', 'r'] 
# using filter function 
filtered = filter(fun, sequence) 
  
print('The filtered letters are:') 
list(filtered)


    
    
    
seq = [0, 1, 2, 3, 5, 8, 13] 
  
# result contains odd numbers of the list 
result = filter(lambda x: x % 2 != 0, seq) 
print(list(result)) 
  
# result contains even numbers of the list 
result = filter(lambda x: x % 2 == 0, seq) 
print(list(result)) 




str1="1010101111010101111"
print(''.join(list(filter(lambda x: x=='0', str1))))




# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)



# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)





