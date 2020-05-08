# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 23:18:20 2018

@author: sky
"""
"""
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
  
"""  

#create simple class
class MyClass:
    """A simple example class"""
    i = 12345
# creating object
MyClass()
x = MyClass()
x.__doc__
print(x.i)


#class with method
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        print(self.i)
        
    def p(self):
        print("value is :",self.i)
    
x = MyClass()
x.i
x.f()
x.p()



#class with constructor
class Complex2:
    tiers=5
    def __init__(self):
        print("construtor is called")
    def fun(self):
        print(self.tiers)
        
x = Complex2()
y=Complex2()
x.tiers =8
y.tiers=7
x.fun()
y.fun()


#class with destructor
class Employee: 
  
    # Initializing 
    def __init__(self): 
        print('Employee created.') 
  
    # Deleting (Calling destructor) 
    def __del__(self): 
        print('Destructor called, Employee deleted.') 
  
obj = Employee() 
del obj 


#passing parameter to constructor
class Complex:
    def __init__(self, realpart, imagpart):
       self.r = realpart
       self.i = imagpart
    def fun(self):
        print("hello")
        
x = Complex(9.0, 8)
x.r
x.i
x.fun()
y = Complex(6, 7)
y.r
y.i


#example
class Complex:
    def __init__(self, realpart, *imagpart):
       self.r = realpart
       self.i = imagpart

x = Complex(3.0, -4.5,6)
x.r
x.i




#class variable and instand variable
class Dog:
    kind = 'canine'  
    name=""       # class variable shared by all instances
    def __init__(self, y):
        self.name = y    # instance variable unique to each instance
d = Dog('Fido')
e = Dog('Buddy')
d.kind                  # shared by all dogs
e.kind 
d.kind ="zxc"
               # shared by all dogs
d.name                  # unique to d
e.name                  # unique to e
d.kind


#class variable and instant variable
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name2):
        self.name = name2    # instance variable unique to each instance
    def fun(self,x):
        self.kind=x
d = Dog('Fido')
e = Dog('Buddy')
d.kind                  # shared by all dogs
e.kind                  # shared by all dogs
d.name                  # unique to d
e.name                  # unique to e
d.fun("fido_dog")
e.fun("buddy_g")


#example
class student:
    _name=""
    _rollno=0
    def fun(self,x,y):
        if(str(x).isalpha() and str(y).isnumeric()):
            self._name=x
            self._rollno=y
        else:
            print("Please enter valid name and roll no.")
    def display(self):
        print(self._name,self._rollno)
    
x=student()
x.fun("rahul",2,)
x.display()
x.name
x.rollno



#example
class Dog:
    def __init__(self, x):
        self.name = x
        self.tricks = []    # creates a new empty list for each dog
    def add_trick(self, y):
        self.tricks.append(y)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
e.tricks

# unexpectedly shared list by all objects
class Dog:
    tricks = []             
    # mistaken use of a class variable
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks                
e.tricks



#example
class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)  


x=Bag() 
y=Bag() 
x.add(1)
x.add(2)
y.addtwice(3)  
x.data
y.data
    
    
    
#sharing class variable by all object (using class name)   
class Employee:
   'Common base class for all employees'
   empCount = 0
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1   
   def displayCount(self):
     print(Employee.empCount)
   def displayEmployee(self):
      print(self.name,self.salary) 
"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()
emp2.displayCount()

"""
Built-In Class Attributes
Every Python class keeps following built-in attributes and they can be accessed using dot operator like any other attribute −


__doc__ − Class documentation string or none, if undefined.

__name__ − Class name.


__bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
"""


class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print( "Total Employee " , Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)
x=Employee()
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__bases__:", Employee.__bases__)






#Destroying Objects (Garbage Collection)

a = 40      # Create object <40>
b = a       # Increase ref. count  of <40> 
c = [b]     # Increase ref. count  of <40> 

del a       # Decrease ref. count  of <40>
b = 100     # Decrease ref. count  of <40> 
c[0] = -1   # Decrease ref. count  of <40> 



#This __del__() destructor prints the class name of an instance that is about to be destroyed −

#!/usr/bin/python

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name,"object destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt2
print (id(pt1), id(pt2), id(pt3) )# prints the ids of the obejcts
del pt1
del pt2
del pt3




#Class Inheritance
"""
class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite
"""

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print( "Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method



#simple inheritence
class Parent:        # define parent class
   def myMethod(self):
      print ('Calling parent method')

class Child(Parent): # define child class
   def myMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.myMethod()         # child calls overridden method



class Foo(object):
   __bar = 42
 
class Quux(object):
   def spam(self):
     print( Foo._Foo__bar)
 
q = Quux()
q.spam()






#operator verloading in class
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
#When the above code is executed, it produces the following result −

Vector(7,8)

#Data Hiding
#An object's attributes may or may not be visible outside the class definition. You need to name attributes with a double underscore prefix, and those attributes then are not be directly visible to outsiders.

class JustCounter:
   __secretCount = 0
   def count(self):
      self.__secretCount += 1
   def display(self):
       print (self.__secretCount)
counter = JustCounter()
counter.count()
counter.display()
print(counter.__secretCount)
