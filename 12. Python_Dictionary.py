# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 15:14:10 2018

@author: sky
"""
#creating dictionary
dict1={}
dict1={1:2,3:4,5:6}
dict2 = {2: [1,2,3], 'Age': 7, 'Class': 'First'}
#print value
print ( dict2['Age'])
print ("dict['Age']: ", dict2['Age'])
dict2 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict2['Name'])

#error when access wrong key
dict2 = {'Name': 'Zara', 'Age': 7, 2:'two','Class': 'First'}
print ("dict['Alice']: ", dict2['Alice'])

#Updating Dictionary

dict2 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict2['Age'] = 8; # update existing entry
dict2['School'] = "DPS School"; # Add new entry

print ("dict['Age']: ", dict2['age'])
print ("dict['School']: ", dict2['School'])

#deletion
dict2 = {'Name': 'Zara', 'Age': 7, 'Class': 'First','Name':'ABC'}
del dict2['Name']; # remove entry with key 'Name'
dict2.clear();     # remove all entries in dict
del dict2 ;        # delete entire dictionary

print( "dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

#dictionary can not access by index
dict2[0]


#functionMethods
dict2 = {'Name': 'Zara', 'Age': 7};
len(dict2)

i=list(dict2.keys())
i=list(i)

i=dict2.values()
i=list(i)


seq = ('name', 'age', 'sex')
dict1 = dict.fromkeys(seq)
dict1 = dict.fromkeys(seq, 10)
seq=[(1,2),(2,3),(3,4)]
dict(seq)

#in python 2.7
dict2 = {'Name': 'Zabra', 'Age': 7}
dict2['Name']
x=dict2.get(('Name','Age'))


dict2 = {'Name': 'Zara', 'Age': 7}
print(dict2.has_key('Age'))
print("Value : %s" %  dict.has_key('Sex'))

dict.setdefault
dict2 = {'Name': 'Zara', 'Age': 7}
dict2.items()
[('Name','Zara'),('Age',7)]


i=str(dict2)

dict2 = {'Name': 'Zara'}
dict2.setdefault()('Age', None)
dict2.setdefault('Sex', None)
print(dict2['Age'])

dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex' : 'female' ,1:2}
s
dict1.update(dict2)
x=dict1+dict2

dict2 = {'Name': 'Zara', 'Age': 7}
dict2.values()

dict = {'Name': 'Zara', 'Age': 7};

#datatype conversion
x=2
x=2.0
x="asd"
x="abc","asd"
x=2+3j
x=True
#only this can be converted into dict
x=[(1,2),(3,5)]
x=(1,2,3)
print(dict(x))
str(dict2)

#some methods
dict2.pop()
x=dict2.pop('Name')
x=dict1.popitem()


i=[(1,2),(3,3)]
i=dict1.sort()#not define
i=dict(i)
max(dict2)
min(dict2)


#dictionary iteration
dict2={1:2,3:5,5:6}
for i in dict2:
    print(i,dict2[i])
    




    
