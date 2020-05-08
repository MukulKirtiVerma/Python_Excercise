 # -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 13:04:12 2018

@author: sky
"""
i=12121211
print('hi {:+10d} my {}'.format(i,i))
"""
string formatingg
1. simple {}
2. {} {}
"""
#add '_' after print value
print('{:_<10}'.format('test'))
#add 10 space before print value 
print('{:^10}'.format('test'))
#print only starting 5 char
print('{:.5}'.format('xylophone'))
#print string then print 10 spaces
print('{:10.5}'.format('xylophone'))
#add space before value
print('{:>5}'.format(333))
#wraoe string to 5 char
print('{:5}'.format(3388))
#wrap string to 5 char and add 0 if string less then 5 char
print('{:05d}'.format(42))
#add + sign
print('{:+d}'.format(42))
#add -ve sign
print('{:-d}'.format(42))
#add space before value
print('{: d}'.format(42))
#wrape string to 5 char and add space if less then 5 char
print('{:=+5d}'.format(23)) 
#add space after
print('{:1d}'.format(42))


#floting point formatting

x=3.141592653589793
#print only 6 floting point digits
print('{:f}'.format(3.141592653589793))
#print only 2 floting points
print('{:.2f}'.format(3.141592653589793))
#print total 6 digit and 2 floting point number
print('{:06.2f}'.format(3.141592653589793))