# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:37:23 2021

@author: Mukul Kirti Verma
"""

def first(msg):
    print(msg)


first("Hello")

second = first
second("Hello")




def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


operate(inc,3)
4
operate(dec,3)
2


def is_called():
    def is_returned():
        print("Hello")
    return is_returned


new = is_called()

# Outputs "Hello"
new()




def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")
    
    
    
ordinary()
I am ordinary

# let's decorate this ordinary function
pretty = make_pretty(ordinary)
pretty()



pretty = make_pretty(ordinary)



ordinary = make_pretty(ordinary).




@make_pretty
def ordinary():
    print("I am ordinary")
    
    
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)




def divide(a, b):
    return a/b

divide(2,5)
0.4
divide(2,0)


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner



def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)
    
    
    
>>> divide(2,5)
I am going to divide 2 and 5
0.4

>>> divide(2,0)
I am going to divide 2 and 0
Whoops! cannot divide




Chaining Decorators in Python
Multiple decorators can be chained in Python.

This is to say, a function can be decorated multiple 
times with different (or same) decorators. We simply 
place the decorators above the desired function.

def star(func):
    def inner(x):
        print("*" * 30)
        #func(x)
        print("*" * 30)
    return inner


def percent(func):
    def inner(x):
        print("%" * 30)
        func(x)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")




@star
@percent
def printer(msg):
    print(msg)
    
is equivalent to

def printer(msg):
    print(msg)
printer = star(percent(printer))
The order in which we chain decorators matter. If we had reversed the order as,

@percent
@star
def printer(msg):
    print(msg)
The output would be:

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
Hello
******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%