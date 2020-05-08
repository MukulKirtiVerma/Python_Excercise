 # -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 09:21:08 2018

@author: Mukul Kirti Verma
"""
#by default all variable are local


def f1():
    x=x+100
    print(x)
x=1
f1()
print(x)


def san(x):
    print(x+1)
x=-2
x=4
san(12)


#if you want to make variable glibal the use key word global
#all global variable should be declare in the bigning
def f1():
    global x
    x+=1
    print(x)
    
x=12
print("x")


#eg.

def f1(x):
    global x
    x+=1
    print(x)
f1(15)
print("hello")


def f():
    global a
    print(a)
    a = "hello"
    print(a) 
a = "world" 
f()
print(a)



#But in the case of iterable object like list tuple dictionary
#by default they are global
def f1(a):
    b.append(a)
    return b
b=[6]
print(f1(2))

#if you initialize a  list tuple or dictionary in fun then it become local

def f1(a,):
    b=[]
    b.append(a)
    return b
b=[6]
print(f1(2))
print(b)


#eg
def f(p, q, r):
    global s
    p = 10
    q = 20
    r = 30
    s = 40
    print(p,q,r,s)
p,q,r,s = 1,2,3,4
f(5,10,15)



#eg
def f(x):
    print("outer")
    def ff1(a):
        print("inner")
        print(a,x)
f(3)
ff1(1)





#eg
x = 5 
def f1():
    global x
    x = 4
def f2(a,b):
    global x
    return a+b+x
f1()
total = f2(1,2)
print(total)


#eg
x=100
def f1():
    global x
    x=90
def f2():
    global x
    x=80
print(x)

#eg
y, z = 1, 2
def f():
    global x
    x = y+z
f()   
    
