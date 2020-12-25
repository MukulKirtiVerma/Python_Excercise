# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:08:45 2018

@author: james
"""

x1= {"a","b","c"}
x1= set({})

x2= {"a","b","d","e"}


x= set(("apple","banana","cherry"))
x.add("damson")
x.add("apple")

print(x)

x = set(("banana","cherry","apple"))
x.remove("banana")
print(x)

x = set(("apple","banana","cherry"))
print(len(x))
x1={1,2,3,4,5}
x2={4,5,6,7,8}

x3=x2.difference(x1)
 
 'copy',
x3=x2.copy()
 'difference',
x3=x2.difference(x1)
 
 'discard',#remove element from x2
x2.discard(8)

 'intersection',
x1={1,2,3}
x2={3,4,5}
x2.intersection(x1)
 'isdisjoint',
 
x1={1,2,3}
x2={1,2}
x2.isdisjoint(x1)
 'issubset',
x2.issubset(x1)
 'issuperset',
x1.issuperset(x2)

 'pop',#remove element from bibning
x2.pop()
 
 'symmetric_difference',
x2.symmetric_difference(x1)
 'union',
x3=x2.union(x1)
 
x2.clear()


for i in x:
    print(i)
 
