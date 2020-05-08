# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:52:49 2018

@author: sky
"""
#Python list is a collection of hetroginous datatyps

#creating list

#list without element
list1=[]
#list with single element
list1=[2]
#list with multiple element
list2=[1,2]
list3 = ['physics', 'chemistry', 1997, 2000]
list4 = [1, 2, 3, 4, 5 ]
list5 = ["a", "b", "c", "d"]

list6=[list1,list2,3]
print(list6)


#Accessing Values in Lists
#1.Indexing, 
#2.Slicing,

#indexing
L = ['hello', 'hi', 'bye']
print(L[0])
print(L[2])
print(L[-2])
list5 = ['hello', 'hi', 'bye']

#slicing
print(list5[1:3])
print(list5[2:])
print(list5[:3])
print(list5[:])
list6=[list1,list2,3]
print(list6[1][0:2])

#slcing
list1 = ['physics', 'chemistry', 1997.8,5j+1, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print("list1[0]: ", list1[0])
print("list1[0]: ", list1[1])

print(list2[1:5])
print(list2[1:])
print(list2[:5])


#Updating Lists

#add element with append method
l=[1,2]
l.append(3)

list2 = ['physics', 'chemistry', 1997, 2000];
#update element
list2[2] = 2001;
list2[5] = 2001;
print(list2)
list2[1:3]=2,5

#Delete List Elements


list1 = ['physics', 'chemistry', 1997, 2000];
#delete single element
del list1[2];
#delete multiple element
del list1[1:3];
#delete all element in list
list1.clear()
#delete whole list
del list1


list1[0]="math"


"""
Basic List Operations

Length len
Concatenation list1+list2
Repetition list1*5
Membership 
Iteration

"""

"""++++lenth+++++====="""
list1=[1,2,3,4,5]
print(len(list1))
"""+++++++++++++++++++++++"""

"""+++++++concatinate++++++"""
list1=[1,2,3,4,5]
list2=['a','b','c','d']
l=list1+list2

"""++++++++Multiply integer to list++++++++++"""

list1=[3,5]
l=list1*5

"""++++++++ Membership of element  +++++++++++++"""

list1=[1,2,3,4,5,6]
3 in list1
3 not in list1

"""++++++++++Iterate list element through for loop++++++++++++++++++"""

for i in list3:
    print(i)
    
for i in range(0,len(list3)):
    print(list3[i])


"""++++++++++++++++iterate through while loop+++++++++++++"""
i=0
list1=[1,2,3,4,5,6]

while(i<len(list1)):
    print(list1[i])
    i=i+1



"""+++++++++++++++way to create list++++++++++++++"""
a=[x**3 for x in range(0,6)]


#some Built-in List Functions & Methods


list1=['hi','hellohi','by']
list2=['ji','ki']

cmp(list1, list2)
#Compares elements of both lists.

len(list1)
#Gives the total length of the list.
list1=[1,2,3,4,5,9,3,10]
max(list1)
min(list1)

list2=['HI','bye','BYE','3']
max(list2)
min(list2)

'0'-'9'
'A'-'Z'
'a'-'z'
#Returns item from the list with min value.


"""++++++++++++++++++"""
#type casting
#run one by one then run list(t)
t="hi"
t=["hi","ki"]
t=6.0
t=True
t=2+3j

t=5
t=(1,2,3)
t={1:2,2:3,5:6}
list(t)

"""++++++++count fun++++++++++++"""

list1=[]
list1.append("bye")
list1=list1*5
list1.count("bye")

list1.count("mkv")
#Returns count of how many times obj occurs in list
list1.append("mkv",'abc')

"""++++++++++extend list with List++++"""
list1.extend([123, 3,6])
#Appends the contents of seq to list


list1.append(["mkv","jki"])

list1.index('bye')
list2.append("bye")
list1.index(['mkv', 'jki'])



#Returns the lowest index in list that obj appears

index=5
list1.insert(5, "hi")
index=50
list1.insert(index, "hi")
index=-1 
list1.insert(index, "hi")

#diffrence b/w del and pop , run line one by one
del L[1]
x=L.pop(1)

"""++++++++++++remove method+++++++++++++++++"""
list2=[1,2,3,4,5,6]
x=list2.pop()
list2.pop(2)
x=list2.remove(2)

list2.reverse()
Reverses objects of list in place

list
list1.sort()
#work only for homoginus datatype