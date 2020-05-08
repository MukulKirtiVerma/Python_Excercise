# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 13:51:27 2018

@author: james
"""

str1="((())))("
      01234567
i=0
l=[]

while(('(' in str1) or (')' in str1)):
    while(str1[i]!=')'):
        i=i+1
    l.append(i) 
    str1=str1[0:i]+'~'+str1[i+1:]
    while(str1[i]!='('):
        i=i-1
    l.insert(0,i) 
    str1=str1[0:i]+'~'+str1[i+1:]
    print(l)
    l=[]
    result

    
