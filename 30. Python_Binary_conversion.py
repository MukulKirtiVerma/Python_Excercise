# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:27:11 2018

@author: james
"""

# syntax int(binary number, base)

"""Binary to decimal(base 2)"""

int("1111",2)
"""
Output:
9"""


"""
Binary to base 3"""
str1="1"
for i in range(15):
    str1=str1+'1'
    print(int(str1,3))
"""
Output:
28"""


"""
Binary to base 5"""
int("1111",5)
"""
Output:
156"""


#binary AND operation
inputA = int('00100011',2)
inputB = int('00101101',2)
print ((inputA & inputB))

#binary XOR
inputA = int('00100011',2)
inputB = int('00101101',2) 
print (bin(inputA ^ inputB))



"""manual code to convert binary to decimal"""
x="0011"
lt=len(x)
y=0
for i in x:
    y=y+(2**(lt-1))*(int(i))
    lt=lt-1
print(y)

"""Decimal to binary Conversion"""
num=8
str2=""
while(num>0 or num>1):
    str2=str(int(num%2))+str2
    num=int(num/2)
print(str2)











