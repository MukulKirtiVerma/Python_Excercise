# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 20:39:29 2018

@author: james
"""

class Employee: 
    'Common base class for all employees' 
    empCount = 0
    def __init__(self, name, salary):
           self.name = name 
           self.salary = salary 
           Employee.empCount += 1 
    def displayCount(self): 
            print ("Total Employee %d" % Employee.empCount) 
    def displayEmployee(self): 
            print ("Name : ", self.name, ", Salary: ", self.salary)
            
emp1 = Employee("Zara", 2000) 
emp2 = Employee("Manni", 5000)
emp1.displayEmployee() 
emp2.displayEmployee() 
print ("Total Employee",Employee.empCount)


#some class method
"""
The getattr(obj, name) − to access the attribute of object.

The hasattr(obj,name) − to check if an attribute exists or not.

The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.

The delattr(obj, name) − to delete an attribute.
"""



getattr(emp1,"empCount")
hasattr(emp1,"empCount")
setattr(emp1,"empCount",5)
delattr(emp1,"empCount")




"""In Built Class Attribute

__dict__   − Dictionary containing the class's namespace.
__doc__    − Class documentation string or none, if undefined.
__module__ − Module name in which the class is defined.
             This attribute is "__main__" in interactive mode.
__bases__  − A possibly empty tuple containing the base classes, 
             in the order of their occurrence in the base class list.
"""

class Employee:
      'Common base class for all employees' 
      empCount = 0
      def __init__(self, name, salary):
           self.name = name 
           self.salary = salary 
           Employee.empCount += 1 
      def displayCount(self): 
           print ("Total Employee %d" % Employee.empCount) 
      def displayEmployee(self): 
           print ("Name : ", self.name, ", Salary: ", self.salary)
emp1 = Employee("Zara", 2000) 
emp2 = Employee("Manni", 5000) 
print ("Employee.__doc__:", Employee.__doc__) 
print ("Employee.__module__:", Employee.__module__) 
print ("Employee.__bases__:", Employee.__bases__) 
print ("Employee.__dict__:", Employee.__dict__ )




#Inheritence
#single inheritence
class User:
    name = ""
    def __init__(self, name):
        self.name = name
        print("super constructer is called")
    def printName(self):
        print("Name  = " + self.name)
class Programmer(User):
      
    def __init__(self, name):
        self.name = name
        print("child constructer is called")
    def doPython(self):
        print("Programming Python")
 
brian = User("brian")
brian.printName()
brian.doPython()
diana = Programmer("Diana")
diana.printName()
diana.doPython()

class User:
    name = ""
    def __init__(self, name):
        self.name = name
        print("super constructer is called")
    def printName(self):
        print("Name  = " + self.name)
 
class Programmer(User):
    def __init__(self, name):
        self.name = name
        print("cild constructer is called")
    def printName(self):
        print("chield Name  = " + self.name)
    def doPython(self):
        print("Programming Python")
 
brian = User("brian")
brian.printName()
 
diana = Programmer("Diana")
diana.printName()
diana.doPython()




#multiple Inheritence

class User:
    name = ""
    def __init__(self, name):
        self.name = name
    def printName(self):
        print ("Name  U= ",  self.name)
class User2:
    name = "" 
    def __init__(self, name):
        self.name = name 
    def printName(self):
        print ("Name  U1= " , self.name) 
class Programmer(User2,User):
    def __init__(self, name):
        self.name = name
    def doPython(self):
        print ("Programming Python") 
brian = User("brian")
brian.printName()
diana = Programmer("Diana")
diana.printName()
diana.doPython()


#Hirarical 
class User:
    name = "" 
    def __init__(self, name):
        self.name = name 
    def printName(self):
        print( "Name  = ", self.name) 
class Programmer(User):
    def __init__(self, name):
        self.name = name 
    def doPython(self):
        print ("Programming Python")
class Programmer2(Programmer):
    def __init__(self, name):
        self.name = name 
    def doPython(self):
        print ("Programming2") 
brian = User("brian")
brian.printName()
 
diana = Programmer("Diana")
diana.printName()
diana.doPython()
diana = Programmer2("xuv")
diana.printName()
diana.doPython()
diana.doPython2()

#Multi level
class User:
    name = ""
 
    def __init__(self, name):
        self.name = name
 
    def printName(self):
        print ("Name  = ",  self.name)
        
class User2(User):
    def __init__(self, name):
        self.name = name
    def user2_fun(self):
        print("user2")
class User3:   
    def __init__(self, name):
        self.name = name
    def user2_fun(self):
        print("user3")

class Programmer(User3,User2):
    def __init__(self, name):
        self.name = name 
    def doPython(self):
        print ("Programming Python")
     
brian = User("brian")
brian.printName()
diana = Programmer("Diana")
diana.printName()
diana.user2_fun()
diana.name



issubclass(User2, User)
isinstance(diana, User)
isinstance(diana, User2)
isinstance(diana, Programmer)
isinstance(brian, User2)

#Method Overloading

class Parent: # define parent class def       
       def myMethod(self,name): 
            print ('Calling parent method') 
       def myMethod(self,name,k): 
            print ('Calling parent method2') 
c = Parent() # instance of child  
c.myMethod("hi",2) # child calls overridden method
c.myMethod(2)


class Parent: # define parent class def       
       def myMethod(self,name,*k): 
            print ('Calling parent method') 
      
c = Parent() # instance of child  
c.myMethod("hi",2) # child calls overridden method
c.myMethod(2)




class Parent:     
       def myMethod(self):
           print ('Calling parent method') 
class Child():
       def myMethod(self):
           print ('Calling child method') 
c1 = Parent()
c2 = Child() # instance of child 
c1.myMethod() #child calls overridden method
c2.myMethod() #child calls overridden method








#Method OverLoading

class Human:
     def sayHello(self,i):
            print(i)
      
             
obj = Human()
obj=Human(2) # Call the method 
obj.sayHello()# Call the method with a parameter 
obj.sayHello('Guido')
obj.sayHello(123)

#Method overridinng

class Human:
     def sayHello(self, name=None):
             if name is not None: 
                   print ('Hello ' , name) 
             else: print( 'Hello ')# Create instance 
obj=Human()# Call the method 
obj.sayHello()# Call the method with a parameter 
obj.sayHello('Guido')
obj.sayHello(123)


class Human:
     def sayHello(self, *name):
             if name is not None: 
                   print ('Hello ' , name) 
             else: print( 'Hello ')# Create instance 
obj=Human()# Call the method 
obj.sayHello()# Call the method with a parameter 
obj.sayHello('Guido',123)
obj.sayHello(123)
print(obj)

#Operator OverLoading in class

class Vector:
         def __init__(self, a, b):
               self.a = a 
               self.b= b
         def __str__(self): 
                    return 'Vector (%d, %d)' % (self.a, self.b) 
         def __add__(self,other): 
                     
                     return Vector(self.a + other.a, self.b + other.b) 
v1 = Vector(2,10) 
v2 = Vector(5,-2)
 
print (v1 + v2)






#Abstract class

class AbstractClass:
    
    def do_something(self):
        pass
    
    
class B(AbstractClass):
    pass
a = AbstractClass()
b = B()




#Polymorphism with class
class India(): 
    def capital(self): 
        print("New Delhi is the capital of India.")   
    def language(self): 
        print("Hindi the primary language of India.")  
    def type(self): 
        print("India is a developing country.") 
class USA(): 
    def capital(self): 
        print("Washington, D.C. is the capital of USA.") 
    def language(self): 
        print("English is the primary language of USA.")   
    def type(self): 
        print("USA is a developed country.") 
  
obj_ind = India() 
obj_usa = USA() 
for country in (obj_ind, obj_usa): 
    country.capital() 
    country.language() 
    country.type() 
  
    
#polymorphism  with class and function    
class India(): 
	def capital(self): 
		print("New Delhi is the capital of India.") 

	def language(self): 
		print("Hindi the primary language of India.") 

	def type(self): 
		print("India is a developing country.") 

class USA(): 
	def capital(self): 
		print("Washington, D.C. is the capital of USA.") 

	def language(self): 
		print("English is the primary language of USA.") 

	def type(self): 
		print("USA is a developed country.") 

def func(obj): 
	obj.capital() 
	obj.language() 
	obj.type() 

obj_ind = India() 
obj_usa = USA() 

func(obj_ind) 
func(obj_usa) 


#protected variable
class a:
    self.__i=9
x=a()
x.__i=0
x.__i

#private variable
class employee:
    def __init__(self, name, sal):
        self.__name=name  # private attribute 
        self.__salary=sal # private attribute
e1=employee("Bill",10000)
e1.__salary



# protected attribute 
class employee:
    _name2= "rahul"  # protected attribute 
    
class g():
    gg=employee()
    gg._name="k"
h=g()


e1=g()
e1._name2
e1.fun()
e1.fun("Bill",10000)
e1._name2
e2=employee()
e2._name2="g"

