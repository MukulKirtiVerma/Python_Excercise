# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 14:31:30 2018 
@author: sky
"""

l=[]
i=0
while(i<5) :
  try:   
       l.append(int(input("Please enter an integer: ")))
       i=i+1
  except:
      pass     
print( "Great, you successfully entered an integer!")

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except:
        print("Please tyr again")
print( "Great, you successfully entered an integer!")




while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError as v:
        print(v)
print( "Great, you successfully entered an integer!")





try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())


except IOError as e:
    print (e)
    
except FileNotFoundError as e:
    print (e)
    

    
    
try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())

except Exception as e:
    print ("I/O error",e)
    
try:
    i=["hi"]
    int(i[0])
except (IndexError, ValueError ):
    print("An Error occurd")
    


try:
    f = open('new.txt')
    s = f.readline()
    i = int(s.strip())


except IOError as e:
    print (e)
    
except :
    print("error")


try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
except (IOError , ValueError):
    print ("An I/O error or a ValueError occurred")
except:
    print ("An unexpected error occurred")
   

try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
finally:
    print("There may or may not have been an exception.")



    
try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
except ValueError:
   print("value error")
   
finally:
    print("There may or may not have been an exception.")
    
    
    
    
try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
except ValueError:
    print ("You should have given either an int or a float")
except ZeroDivisionError:
    print ("Infinity")
finally:
    print("There may or may not have been an exception.")
    
 
    
    
# A python program to create user-defined exception
 
# class MyError is derived from super class Exception
class MyError(Exception):
    # Constructor or Initializer
    def __init__(self, value):
       
        self.error=value
        
try:
    i=int(input())
    if(i<6):
        error=MyError(i)
        raise(error)
    print("enterd input is:", i) 
# Value of Exception is stored in error
except MyError as e:
    print(str(e)+"no is less then 6")
    
    
    
    
    
class MyError(Exception):
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
        self.value2=value+1
        
try:
    i=int(input())
    if(i<6):
        
        raise(MyError(i))
    print("enterd input is:", i) 
# Value of Exception is stored in error
except MyError as error:
    
    print(error.value2)



class TransitionError(Exception):
 
    def __init__(self, prev, nex, msg):
        self.prev = prev
        self.next = nex
        self.nn=nex+3
        # Error message thrown is saved in msg
        self.msg = msg
try:
    raise(TransitionError(2,3*2,"Not Allowed"))
 

except TransitionError as error:
    print('Exception occured: ',error)
    
    
    
    
def functionName( level ):
   if level <1:
      raise Exception(level)
      # The code below to this would not be executed
      # if we raise the exception
  

try:
   l = functionName(-10)
   print ("level = ",l)
except Exception as e:
   print ("error in level argument",e.args[0])
    
    
#!/usr/bin/python
AssertionError



def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(2))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))


AttributeError

tup=(1,2,3,4,4)
tup.append(2)

TypeError

len(33)
len(2.0)
len(2+3j)




FloatingPointError

float()




#Syntex Error

import numpy asd




ImportError

from pandas import asd



IndexError
tup=(1,2,3)
tup[1:9]
tup[9]

NameError
ja=kk



NameError
def fun():
    pass
x=fun1()


KeyError
dicte={1:2,2:2,3:3}
dicte[5]




i=0
l=[]
s_int=0
s_float=0
s_str=0
while(i<3):
    n=input()
    try:
        n=int(n)
        if(s_int==0):
            l.append(n)
            i=i+1
            s_int=1
    except:
        try:
            n=float(n)
            if(s_float==0):
                l.append(n)
                i=i+1
                s_float=1
        except:
            n=str(n)
            if(s_str==0):
                l.append(n)
                i=i+1
                s_str=1
        


"""
Some common error:
AssertionError	Raised when assert statement fails.
AttributeError	Raised when attribute assignment or reference fails.
EOFError	Raised when the input() functions hits end-of-file condition.
FloatingPointError	Raised when a floating point operation fails.
GeneratorExit	Raise when a generator's close() method is called.
ImportError	Raised when the imported module is not found.
IndexError	Raised when index of a sequence is out of range.
KeyError	Raised when a key is not found in a dictionary.
KeyboardInterrupt	Raised when the user hits interrupt key (Ctrl+c or delete).
MemoryError	Raised when an operation runs out of memory.
NameError	Raised when a variable is not found in local or global scope.
NotImplementedError	Raised by abstract methods.
OSError	Raised when system operation causes system related error.
OverflowError	Raised when result of an arithmetic operation is too large to be represented.
ReferenceError	Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError	Raised when an error does not fall under any other category.
StopIteration	Raised by next() function to indicate that there is no further item to be returned by iterator.
SyntaxError	Raised by parser when syntax error is encountered.
IndentationError	Raised when there is incorrect indentation.
TabError	Raised when indentation consists of inconsistent tabs and spaces.
SystemError	Raised when interpreter detects internal error.
SystemExit	Raised by sys.exit() function.
TypeError	Raised when a function or operation is applied to an object of incorrect type.
UnboundLocalError	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError	Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError	Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError	Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError	Raised when a Unicode-related error occurs during translating.
ValueError	Raised when a function gets argument of correct type but improper value.
ZeroDivisionError	Raised when second operand of division or modulo operation is zero.
"""