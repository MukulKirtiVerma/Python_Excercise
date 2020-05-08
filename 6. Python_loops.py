# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 15:36:24 2018

@author: sky
"""
"""
python has four type of loop:
1.for loop
2.for else loop
3.while loop
4.while else loop
"""

#for loop
#python for loop is differ from other language for loop
#in python ,for loop is used to iterate the iterable object
#loop with range function
for i in range(1,10):
    print(i)

#for else
#if for loop completely run then else run
for i in range(1,10):
    print(i)
else:
    print(i)    

#-ve for loop start from 10 to 1
for i in range(10,0,-1):
    print(i)
else:
    print(i)    
    
#loop increment by 2
for i in range(0,10,2):
    print(i,end="")


#if we update the iterator variable in inside the loop
#it will not effect the loop
for i in range(0,10):
    print(i)
    i=i+2
print("checked")
    

#while loop
#while loop is similer to other language just differ in declaration .

i=0    
while(i<10):
    print(i)
    i=i+2



#eg.    
"""print
    *
   * *
  * * *
"""  
  
  
i=1
while(i<=4):
    j=4-i
    while(j>=1):
        print(" ",end="")
        j=j-1
    j=1
    while(j<=i):
        print("* ",end="")
        j=j+1
    print("")
    i=i+1

   
#=====================================
    
#eg 
"""
1   2   
2   4
3   6
4   8
5   10
6   12
7   14
8   16
9   18
10  20   
"""   
  
for i in range(1,11):
    for j in range(0,1):
        
        print(i,end="   ")
        print(i*2, end="  ")
    print()
    
#====================================

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

# Output: The sum is 48
print("The sum is", sum)


# Output: range(0, 10)

#===============================
print(range(10))

# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))

# Output: [2, 3, 4, 5, 6, 7]
print(list(range(2, 8)))

# Output: [2, 5, 8, 11, 14, 17]
print(list(range(2, 20, 3)))
#================================

#iterate list from fol loop
genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
	print("I like", genre[i])


#eg
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")



#eg check vovel ant const.
i=0
j="python is awesome"
jj="aeiou"
l=len(j)
while(i<l):
    
    ii=0
    g=0
    
    while(ii<5):
        if(jj[ii]==j[i]):
            print(j[i],"->V")
            g=1
            break
        ii=ii+1
    if(g==0 and j[i]!=" "):
        print(j[i],"->C")
    i=i+1
else:
    print("string is checked")    
      


#iterate string from "for loop"
j="aeiou"
for i in j:
    if(i in jj):
        print(i,"--> V")
    else:
        pass
print("string is checked")    


number = 2 

# Condition of the while loop
while number < 5 :  
    # Find the mod of 2
    if number%2 == 0:  
        print("The number "+str(number)+" is even")
    else:
        print("The number "+str(number)+" is odd")
    number+=1

 
#eg       
languages = ['R', 'Python',  'Scala', 'Java', 'Julia']

for index in range(len(languages)):
   print('Current language:', languages[index])


#eg
number = 2  

while number < 5 :
    print("Thank you")
    # Increment `number` by 1
    number = number+1


#print fibbonaci 
fib_no = 55

# Set `first_no` to 0
first_no = 0

# Set `second_no` to 1
second_no = 1

# Set the counter `count` to 0 
count = 0

# while loop to print the fibonacci series until the `fib_no`
while first_no <= fib_no:
       # Print `first_no`
       print(first_no)
       
       # Fibonnacci number
       nth = first_no + second_no
    
       # update values of `first_no` and `second_no`
       first_no = second_no
       second_no = nth
       
       # Set counter `count` +1
       count += 1

# Initialize `first_no` to `0`
first_no = 0

# Initialize `second_no` to `1`
second_no = 1
           
# Initialize `numbers`
numbers = range(0,11)

# Find and display Fibonacci series
for num in numbers:
           if(num <= 1):
           # Update only `nth`
                      nth = num
           else:
           # Update the values `nth`, `first_no` and `second_no`
                      nth = first_no + second_no
                      first_no = second_no
                      second_no = nth

           # Print `nth`
           print(nth)


"""print:
12321
 232
  3
"""
i=1
while(i<=3):
    j=1
    while(j<i):
        print(" ",end="")
        j=j+1
    j=i
    while(j<=3):
        print(j,end="")
        j=j+1
    j=2
    while(j>=i):
        print(j,end="")
        j=j-1
    print()
    i=i+1

  

#-ve loop will not run if you not pass -1 as third param.
for x in range(11, 1):
    for y in range(11, 1):
        print ((x, y, x*y))
        
        
#break statment in for loop
#break statment stop the loop immediatly  and control come outn of loop
#and exicute next line
for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print ('Current Letter :', letter)
  
#continue statment with while
var = 10                    # Second Example
while var > 0:              
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
      break

print( "Good bye!")



#continue statment send control to the loop
#
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

#
var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good bye!")


#
for i in range(10):
  print(i)
for i in range(1,10):
  print(i)
for i in range(1,10,2):
  print(i)
for i in range(10,1,-2):
  print(i)
  
#for loop with enumerate
#enumerate function return index and element
for i, c in enumerate('test'):
    print(i, c)
  
#zip function combine the iterable object:
for i, j in zip(range(10), range(5,18,2)):
    print(i,j)
  
#eg 
for i in (('hiiiii',2)):
    print(i)
 
for i, c in enumerate('kkkkkk'):
    print( i, c)
    
#enumerate with start index
for i, c in enumerate('kkkkkk',start=2):
    print( i, c) 
#enumerate with start and end index
for i, c in enumerate('kkkkkk',start=2, end=5):
    print( i, c)
    
#for loop with string slice   
string="hjkkjkjk"    
for c in string[0:3]:
    print(c)
