# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:25:17 2018

@author: james
"""

#convert by string library
import string
string.ascii_lowercase[:26]
string.ascii_uppercase[:26]
string.digits[:]
string.hexdigits[:]
string.octdigits[:]
string.punctuation[:]
string.ascii_letters
string.whitespace
st="python is awesome"
string.capwords(st," ")


#Convert by code 
for i in range(ord('a'), ord('z')+1):
    print (i,chr(i))

for i in range(ord('A'), ord('Z')+1):
    print (i,chr(i))

for i in range(ord('0'), ord('9')+1):
    print (chr(i))
li=[]
for i in range(ord('!'), ord('~')+1):
    if((i in range(ord('a'), ord('z')+1)) or i in (range(ord('A'), ord('Z')+1)) or i in (range(ord('0'), ord('9')+1))):
           pass
    else:
       print(chr(i))
    
      

    
    