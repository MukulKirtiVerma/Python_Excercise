# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 01:04:51 2018

@author: sky
"""
#simple generator
def simpleGeneratorFun():
    yield 1           
 
# Driver code to check above generator function
x=simpleGeneratorFun()
print(x.__next__())
 
    
#generate multiple    
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
  
# x is a generator object
x = simpleGeneratorFun()
 
# Iterating over the generator object using next
print(x.__next__()); # In Python 3, __next__()
print(x.__next__()); # In Python 3, __next__()
print(x.__next__()); # In Python 3, __next__()

print(x.close());    
   



#copmarison with return keyword
def squre(num):
    result = []
    for i in num:
        result.append(i*i)
    return result
my_num=squre([1,2,3,4,5,6])

print(my_num)


def squre(num):
    for i in num:
        yield (i*i)
    
my_num=squre([1,2,3,4,5,6])
for num in my_num:
    print(num)



#example 2
def firstn(n):
      num = 0
      
      while num < n:
          num =num+1
      return num

x= firstn(1000000000000)
print("And the sum is..." ,(x))


#example 
def firstn(n):
      num = 0
      while num < n:
          yield num
          num += 1

for random_number in firstn(10000000000000000):
       print("And the sum is..." ,(random_number))



#example
import random

def lottery():

    for i in range(6):
        yield random.randint(1, 40)
    
    yield random.randint(55,56)

for random_number in lottery():
       print("And the next number is..." ,(random_number))
       
       
def num(max):
    number = 1
    while number < max:
        number += 1
        if (number%2):
            yield number
num = num(100000000000)
print(num)
for x in num:
    print(x)