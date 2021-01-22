# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:28:53 2021

@author: Mukul Kirti Verma
"""


Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, 
meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which 
implements the iterator protocol, which consist of the methods __iter__() and __next__().

Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects.
 They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))



mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
  
  
  
mystr = "banana"

for x in mystr:
  print(x)