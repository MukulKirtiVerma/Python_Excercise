# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 11:36:58 2018

@author: james
"""

i=6
if (i<10 and i>5) :  
      print("Number is Less then 10 and > 5")
      
    
else:
       print("Number is greater then 10")




i=2
if(i<10):  
    print("Number is Less then 10")
    if(i>5):
          print("number is greater then 5")
if(i>10):
     print("Number is greater then 10")
       
       
i=8
if(i<10):
      print("Number is Less then 10")
      if(i<5):
          print("no is < 5")
      else :
          print("no is greater then 5")
else:
     print("Number is greater then 10")
     

i=10
if(i<10):
      print("Number is Less then 10")
elif(i>10):
      print("no is > 10")
else :
      print("10")
"""
Qus 3,5,7 divisibility
10-20,20-30,30-40
"""

i=int(input("enter the value"))
if(i<10):
        print("Number is in b/w 1- 10")
        if(i%2==0):
            print("number is even")
        else:
            print("number is odd")
elif(i<20):
        print("Number is in b/w 10- 20")
elif(i<30):
        print("Number is in b/w 20- 30")


i=input()
if('.' in i):
    print("vlaue is float")
else:
    print("vlaue is int")
    