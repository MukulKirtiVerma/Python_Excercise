# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:08:45 2018

@author: james
"""
"""
Mathematically a set is a collection of items not in any 
particular order. A Python set is similar to this mathematical 
definition with below additional conditions.

The elements in the set cannot be duplicates.
The elements in the set are immutable(cannot be modified) 
but the set as a whole is mutable.
There is no index attached to any element in a python set. 
So they do not support any indexing or slicing operation.
"""
#Set Operations
#The sets in python are typically used for mathematical 
#operations like union, intersection, difference and complement etc.
#We can create a set, access it’s elements and carry out these 
#mathematical operations as shown below.

"""=======================================================================
Creating a set
#A set is created by using the set() function or placing all the elements within a pair of curly braces.
"""
 
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}

print(Days)
#===============================================================
print(Months)
#===============================================================
print(Dates)
#===============================================================

#Typecast tuple to set===============================================================
x= set(("apple","banana","cherry"))
#===============================================================

"""=============================================================
Adding Items to a Set
We can add elements to a set by using add() method. Again as discussed there is no specific index attached to the newly added element.
"""
 
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
 
Days.add("Sun")
print(Days)


#===============================================================
"""
Removing Item from a Set
We can remove elements from a set by using discard() method. Again as discussed there is no specific index attached to the newly added element.
""""
 
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
 
Days.discard("Sun")
print(Days)

"""
Union of Sets
The union operation on two sets produces a new set containing all 
the distinct elements from both the sets. In the below example the 
element “Wed” is present in both the sets.
"""
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)


"""
Intersection of Sets
The intersection operation on two sets produces a new set 
containing only the common elements from both the sets.
In the below example the element “Wed” is present in both the sets.
"""
 
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
print(AllDays)

"""
Difference of Sets
The difference operation on two sets produces a new set 
containing only the elements from the first set and none 
from the second set. In the below example the element “Wed” 
is present in both the sets so it will not be found in the 
result set.
"""
 
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA - DaysB
print(AllDays)

"""
Compare Sets
We can check if a given set is a subset or 
superset of another set. The result is True or 
False depending on the elements present in the sets.
"""

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)


"""
Iterate set 
"""
for i in x:
    print(i)

x = set(("apple","banana","cherry"))
print(len(x))
x1={1,2,3,4,5}
x2={4,5,6,7,8}

"""
'isdisjoint',
"""
 
x1={1,2,3,7}
x2={1,2,7}
x2.isdisjoint(x1)

"""
'issubset',
"""
x2.issubset(x1)

"""
'issuperset',
"""
x1.issuperset(x2)


"""
'pop',#remove element from bigning
"""
x2.pop()
 

#delete all element
x2.clear()


