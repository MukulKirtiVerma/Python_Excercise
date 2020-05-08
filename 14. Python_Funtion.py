# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 17:53:17 2018

@author: sky
"""

#define a function
def fun():
    print("hello")
    
#function calling    
fun()

#parameter passing to function
def fun(j):
    print(j)
fun(2)


#multiple parameter passing
def fun(x,y):
    print(x+y)  
    
x=fun(2,3)#default return type of a function is None
fun(4,5)


def sum2(x,y):
    print(x+y)
k=sum2(2,3)
k=sum2(100,1)

#function documentation
def functionname( ):
   "function_docstring"
   return
 
functionname().__doc__()


#fun accept any type of value
def printme(i):
   "This prints a passed string into this function"
   print (i)
   
#example   
printme(2)
print("Hello")

#example
def printme( i ):
   print (i)
   return i+"b"
printme('ok')


#example
def fun(y):
    print(y)
fun([1,2,3])
printme("a")
x=printme("a")
printme("Again second call to the same function")


 
#call by reference in the case of list tuple dict
# Function definition is here
def changeme( mylist ):
   mylist.extend([1,2,3,4]);
   print( mylist )
   return 

# Now you can call changeme function
mylist=[1,2]
changeme(mylist)
print(mylist)

"""
You can call a function by using the following types of formal arguments −

Required arguments
Keyword arguments
Default arguments
Variable-length arguments
"""


#Required arguments
# Function definition is here
def printme( x ):
   "This prints a passed string into this function"
   print( x )
   return;

# Now you can call printme function
printme(2)


#keyword arguments
def fun(name,age):
    print(name,age)
    
fun(age=23,name="rahul")      
fun(age=23,name="xyz")    


#example keyowd and positional arguments
def printme(y,str,i):
   "This prints a passed string into this function"
   print (y,str,i)
   return;

# Now you can call printme function
printme(2,i="j",str="hi")



# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )





def fun(name,section="A"):
    print(name ,section)
fun("xyz")
fun("xyz","B")


def fun(x,z,y=3):
    print(x,y,z)
fun(1,z=6)






# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ( name)
   print ( age)
   return;
# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )



#Variable-length arguments
# some c language example
"""
void fun(x,y):
    print(x+y)

fun(2,3,5)




void fun(x,y):
    print(x+y)
void fun(x,y,z):
    print(x+y+z)
fun(2,3,5)
fun(2,5)


void fun(x,y):
    print(x+y)
void add(x,y):
    print(x-y)
fun(x-y)

"""




#variable llength argument in python , similer to function overloading
# Function definition is here
def printinfo( arg1,arg2,*vartupl ):
   print(arg1,":",arg2,":",vartupl)
   x=arg1+arg2
   for var in vartupl:
       x=x+var
   return x

# Now you can call printinfo function
#printinfo( 10 )
printinfo(2,3,4,6,7)

def printinfo( arg1,arg,*vartuple ):
   "This prints a variable passed arguments"
   print( "Output is: ")
   print (arg1,vartuple)
   for var in vartuple:
      print (var)
   return;

# Now you can call printinfo function
#printinfo( 10 )
printinfo( 70,9,80)

def printinfo(arg1,arg2,*x,**agr ):
   "This prints a variable passed arguments"
   print(arg1,arg2,x,agr)
   
# Now you can call printinfo function
#printinfo( 10 )
printinfo( 70,9,10,11,15,h=8,i=9,k=8)




# Function definition is here Anonymous
#Anonymos functions
sum2 = lambda arg1, *arg2: arg1 + max(arg2)

# Now you can call sum as a function
print( "Value of total : ", sum2( 10, 20,60,80))
print ("Value of total : ", sum2( 20, 20 ))


# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print("Inside the function : ", total)
   return arg1+arg2;

# Now you can call sum function
total = sum( 10, 20 );
print("Outside the function : ", total )

"""
Global variables
Local variables
"""
# Function definition is here
def sum2( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print (total)
   
total = 0; # This is global variable.

# Now you can call sum function
sum2( 10, 20 );
print(total)


# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   
   mylist = [1,2,3,4];
   mylist.append(1)# This would assig new reference in mylist
   print(mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print( mylist)


def sum2(y):
    
    y.append(2)
    print(y)
x=[3]
sum2(x)
print(x)

#global variable
total = 0; # This is global variable.
# Function definition is here
def sum(  ):
   # Add both the parameters and return them."
   global total 
   total= 20; # Here total is local variable.
   print ("Inside the function local total : ", total)

# Now you can call sum function
sum( )
print("Outside the function global total : ", total)




# This function uses global variable s 
def f():  
    print (s)  
  
s = "This function uses variable s"
f() 



# This function has a variable with 
# name same as s. 
def f():  
    s = "Me too."
    print (s ) 
  
# Global scope 
s = "This function uses global variable s" 
f() 
print (s) 




def f():
    global s
    print (s) 
    # This program will NOT show error 
    s = "Me too."
    print(s) 
# Global scope 
s = "This function uses global variable s" 
f() 
print (s) 




# This function modifies global variable 's' 
total=0
def fun(a,b):
    global total
    total=a+b
fun(2,3)
print(total)



def f(): 
    
    print(s) 
    s ="hi"
    print(s)
  
# Global Scope 
s = "Python is great!" 
f() 
print (s )




def f(): 
    print(s) 
    global s
    s='hi'
    print(s)
# Global Scope 
s = "Python is great!" 
f() 
print (s )



def f(): 
    global s
    print(s) 
    s ="hi"
    print(s)
# Global Scope 
s = "Python is great!" 
f() 
print (s )


#example local and global variable
a = 1
# Uses global because there is no local 'a' 
def f(): 
    print ('Inside f() : ', a )  
# Variable 'a' is redefined as a local 
def g():     
    a = 2
    print ('Inside g() : ',a)  
# Uses global keyword to modify global 'a' 
def h():
    global a 
    a = 3
    print ('Inside h() : ',a )  
# Global scope 
print ('global : ',a )
f() 
print ('global : ',a )
g() 
print ('global : ',a )
h() 
print ('global : ',a )


#example
a=5
def f():
    print(a)
def g():
    a=3
    print(a)
    f()
    print(a)
    h()
def h():
    g()
    f()
g()
h()
print(a)

def fun(i):
    if(i==0):
        return
    else:
        
        fun(i-1)
        print(i)
fun(5)
   










def h():
    print("hello")
    h()
h()



