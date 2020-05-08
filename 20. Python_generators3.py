# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 01:04:51 2018

@author: sky
"""

def simpleGeneratorFun():
    yield 1           
 
# Driver code to check above generator function
x=simpleGeneratorFun()
print(x.__next__())
 
    
    
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
  
# x is a generator object
x = simpleGeneratorFun()
print(x.__next__())

# Iterating over the generator object using next
print(x.__next__()); # In Python 3, __next__()
print(x.close());    
   




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




def firstn(n):
      num = 0
      
      while num <= n:
          num =num+1
      return num

x= firstn(100000000000)
print("And the sum is..." ,(x))


 
def firstn(n):
      num = 0
      while num < n:
          yield num
          num += 1

for random_number in firstn(100000000):
       print("And the sum is..." ,(random_number))





       
       
def num(max):
    number = 1
    while number < max:
        number += 1
        if (number%2):
            yield number
num = num(100)
for x in num:
    print(x)
print("HI")




def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n  
# It returns an object but does not start execution immediately.
a = my_gen()

# We can iterate through the items using next().
next(a)

 # Once the function yields, the function is paused and the control is transferred to the caller.

# Local variables and theirs states are remembered between successive calls.
next(a)
#This is printed second
2

next(a)
#This is printed at last
3

# Finally, when the function terminates, StopIteration is raised automatically on further calls.
next(a)




#Python Generator Expression

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
[x**2 for x in my_list]

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
(x**2 for x in my_list)





my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)
# Output: 1
print(next(a))

# Output: 9
print(next(a))

# Output: 36
print(next(a))

# Output: 100
print(next(a))

# Output: StopIteration
next(a)