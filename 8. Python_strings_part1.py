# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 13:22:09 2018

@author: sky
"""
"""========================================================================"""
"""
#1 Strings are amongst the most popular types in Python. We can 
create them simply by enclosing characters in quotes. 
Python treats single quotes the same as double quotes.
Creating strings is as simple as assigning a value to a variable. 
For example −
"""


var1 = 'Hello World!'
str1 = "python is Awesome."
#Access chatecter of string
"""
Accessing Values in Strings=============================================
Python does not support a character type; these are treated as 
strings of length one, thus also considered a substring.
To access substrings, use the square brackets for slicing along with the index or indices to obtain your substring. For example −"""
str1[10]
str1[20]

#string Sloce=====================================================
str1[3:11]
str1[5:]
str1[:5]
str1[:]
str1[-2]
str1[-5:-2]
str1[-2:-5]
str1[-1:-5:-1]
str1[-5:20]
str1[0:18:2]
str1[20:0:-2]
str1[::-1]

#string concatinate==============================================
i="hi"
j="hello"
k=i+j

#iterate string==================================================
for i in str1:
    print(i)
    
#iterate through while loop======================================
    
i=0
while(i<=len(str1)):
    print(str1[i])
    i=i+1

#iterate with for loop and  with index=========================== 
for i in range(0,len(str1)):
    print(str1[i])
    

#string Methods==================================================


#Capitalizes first letter of string
string=str1
print(str1.capitalize())

string = "a abc is aN operator."

new_string = string.capitalize()

print('Old String:', string)
print('New String:', new_string)

"""========================================================================="""

#string concatinate
str1="python is Awesome."
str2=" good to know that" 
str3=str1+str2


"""======================================================================="""

#center syntex string.center(width,fillchar)
string = "Python"
new_string = string.center(30)
print("Centered String: ", new_string)
                                                        
#2==================================================================
string = "Python is awesome"

new_string = string.center(24, '@')

print("Centered String: ", new_string)

"""========================================================================"""
#casefolds syntex : string.casefold()

string = "PYTHON IS AWESome3"

# print lowercase string
print(string.casefold())
"""========================================================================="""
#count syntex : string.count(substring, start=..., end=...)
#Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.
# define string
string = "Python is awesome is , isn't it?"
substring = " is"
count = string.count(substring)
print("The count is:", count)

string = "Python is awesome, isn't it?"
substring = "is"

# count after first 'i' and before the last 'i'
count = string.count(substring)

# print count
print("The count is:", count)

 'i'
count = string.count(substring,6 ,13)

# print count
print("The count is:", count)



"""========================================================================="""

#endwith syntex str.endswith(suffix, start, end)
#Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise.
text = "Python is easy to learn."

result = text.endswith('n.')
result = text.endswith('n')

#==========================================================
result = text.endswith('Python is easy to learn.')
# returns True
print(result)

#==========================================================
result = text.endswith('Python is easy to learn.')
# returns True
print(result)

result= i.endswith(('gmail.com','yahoo.com','msn.com'))


text = "Python programming is easy to learn."

# start parameter: 7
# "programming is easy to learn." string is searched
result = text.endswith('learn.' )
print(result)

# Both start and end is provided
# start: 7, end: 26
# "programming is easy" string is searched

text="Python programming is easy to learn."
text[7:30]

result = text.endswith('to ', 7, 30)
# Returns False
print(result)

result = text.endswith('easy', 7, 26)
# returns True
print(result)



text = "programming is easy"
result = text.endswith(('programming', 'easy'))

# prints False
print(result)

result = text.endswith(('python', 'easy', 'java'))

print(result)

# With start and end parameter
# 'programming is' string is checked


result = text.endswith(('is', 'eas'), -5, -1)

# prints True
print(result)



#startswith(str, beg=0,end=len(string))
#Determines if string or a substring of string (if starting index beg and ending index end are given) starts with substring str; returns true if so and false otherwise.

openb='('
closeb=')'
i=str(input("Enter a braces pattern  "))
if  not i.startswith(openb):
    print("open brace is not given first")
    
if not i.endswith(closeb):
    print("close brace is not given at end")

if(i.count(openb)!=i.count(closeb)):
    print("Invalid pattern")    
else:
    print("Good pattern given")


"""========================================================================="""

         
#index(str, beg = 0, end = len(string))
#Same as find(), but raises an exception if str not found.

 

sentence = 'Python   is programming and it is fun.'

result = sentence.index('is')
print("Substring 'is fun': at ", result)

result = sentence.index('Java')
print("Substring 'Java':", result)

"""=================================================================
rindex( str, beg = 0, end = len(string))
Same as index(), but search backwards in string."""


sentence = 'Pythonis      is programming is fun.'
sentence[14]
# Substring is searched in 'gramming is fun.'
print(sentence.rindex('is'))

# Substring is searched in 'gramming is '
print(sentence.index('is', 10, -4))

# Substring is searched in 'programming'
print(sentence.index('is', 8, 18))


quote = 'Let it be, let it be, let it be'


result = quote.rindex('let it')
print("Substring 'let it':", result)
 
#2
quote = 'Do small things with great love'

# Substring is searched in ' small things with great love' 
print(quote.rindex('t', 2))

# Substring is searched in 'll things with'
print(quote.rindex('th', 6, 20))

# Substring is searched in 'hings with great lov'
print(quote.rindex('o small ', 10, -1))

"""========================================================================"""
#isalnum syntex:string.isalnum()
"""
isalnum()
Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.
"""

name = "M234onica"
print(name.isalnum())

# contains whitespace
name = "M3onica Gell22er "
print(name.isalnum())

name = "Mo3nicaGell22er@"
print(name.isalnum())

name = "133"
print(name.isalnum())


"""=================================================================
isalpha()
Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.
"""
name.isalpha()


"""========================================================================="""
#isdigite syntex :string.isdecimal()

#1
s = "28.2129"
s='9A'
print(s.isdecimal())
s = "28212A"
print(s.isdecimal())
# contains alphabets
s = "32ladk3"
print(s.isdecimal())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdecimal())

#2
s = '111111'
print(s.isdecimal())

s = '1/2'
s='3²455'
s = '½'
print(s.isdecimal())
s=int(s)

"""========================================================================="""
"""
isdigit()
Returns true if string contains only digits and false otherwise.
#isdigit syntex :string.isdigit()"""
s = "28212"
print(s.isdigit())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdigit())


s = '23455'

print(s.isdigit())

s = '3455²'
# subscript is a digit
s = '3455\u00B2'
print(s.isdigit())

s = '½'
# fraction is not a digit
s = '\u00BD'
print(s.isdigit())

"""========================================================================="""
#isnumeric syntex :string.isnumeric()
"""
isnumeric()
Returns true if a unicode string contains only numeric characters and false otherwise.
"""
s = '1242323'
print(s.isnumeric())

#s = '²3455'
s = '\u00B23455'
print(s.isnumeric())

s = '½'
s = '\u00BD'
s='0.8'
print(s.isnumeric())

s = '12423/23'
s = '-12423'
s='0.8'

print(s.isnumeric())
"""========================================================================="""

#isidentifire syntex  :string.isidentifire()

str2 = 'Python'
print(str2.isidentifier())

str2 = 'Py thon'
print(str2.isidentifier())

str2 = '22'
print(str2.isidentifier())


str2 = 'i22'
print(str2.isidentifier())

str2 = ''
print(str2.isidentifier())


str2 = 'Python2'
print(str2.isidentifier())
str2 = '@Python'
print(str2.isidentifier())
str = 'Py@thon'
print(str.isidentifier())
str = 'Python@'
print(str.isidentifier())
str2 = '_Python'
print(str2.isidentifier())
str2 = '_9'
print(str2.isidentifier())
str2 = '__ABC__'
print(str2.isidentifier())



"""========================================================================="""

#islower syntex:   string.islower()
#islower Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.
#isupper - Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.
s = 'THIS is good'
print(s.upper())
s = 'th!s 111...1is a1so g00d'
print(s.upper())

s = 'THIS is good'
print(s.lower())
s = 'th!s 111...1is a1so g00d'
print(s.lower())



s = 'th!s 111...1is a1so g00d'

print(s.islower())

s = 'this is Not good'
print(s.islower())

s = 'th!s 111...1is a1so g00d'

print(s.isupper())

s = 'PYTHON'
print(s.isupper())



"""========================================================================="""
#isprintable syntex: string.isprinteble()

#1
s = 'Space is a printable'
print(s)
print(s.isprintable())

s = '\tNew Line is printable'
print(s)
print(s.isprintable())

s = ' '

print(s.isprintable())



s = ''
print('\nEmpty string printable?', s.isprintable())

"""========================================================================="""
#isspace()  syntex: string.isspace()


#Returns true if string contains only whitespace characters and false otherwise.


s = '   t'
print(s.isspace())

s = ' a '
print(s.isspace())

s = ' '
print(s.isspace())


s = '\t'
print(s.isspace())

s = '\n'
print(s.isspace())
h="hello\r hi"
s = '\r'
print(s.isspace())

s = '\f'
print(s.isspace())



"""========================================================================="""
#string.istitle()
#Returns true if string is properly "titlecased" and false otherwise.

s = 'Python Is Good.'
print(s.istitle())

s = 'Python is good'
print(s.istitle())

s = 'This Is @ymbol.'
print(s.istitle())

s = 'This 1Is @Symbol.'
print(s.istitle())

s = '99 9I9S A Number'
print(s.istitle())

s = 'PYTHON'
print(s.istitle())


"""========================================================================="""


#Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.

s1 = 'abcghi'
s1 = '123456'
s2 = ','
s2 = '123456'
s1 = 'abcghi'
s2 = '1'

""" Each character of s2 is concatenated to the front of s1""" 
print(s1.join(s2))

""" Each character of s1 is concatenated to the front of s2""" 
print(s2.join(s1))



numList = ['1', '2', '3', '4']
seperator = ', '
print(seperator.join(numList))

numTuple = ('1', '2', '3', '4')
print(seperator.join(numTuple))




test =  {'2', '1', '3'}
s = ', '
print(s.join(test))

test = {'Python', 'Java ', 'Ruby'}
s = '->->'
print(s.join(test))

"""========================== ==============================================="""
#Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.
string = 'cat'
width = 5
# print left justified string
print(string.ljust(width))
"""========================================================================="""
#string.rjust(width, fillchar)
string = 'cat'
width = 5

#Returns a space-padded string with the original string right-justified to a total of width columns.
print(string.rjust(width))
string = 'cat'
width = 5
fillchar = '*'

# print right justified string
print(string.rjust(width, '*'))

"""========================================================================="""



#string.swapcase()
# Inverts case for all letters in string.


string = "THIS SHOULD ALL BE LOWERCASE."
print(string.swapcase())

string = "this should all be uppercase."
print(string.swapcase())

string = "ThIs ShOuLd Be MiXeD cAsEd."
print(string.swapcase())


"""========================================================================="""
# string.lstrip([chars])
#lstrip()
#Removes all leading whitespace in string.

random_string = '   strthis is good '

# Leading whitepsace are removed
print(random_string.lstrip())
random_string = 'str this is good '

# Argument doesn't contain space
# No characters are removed.
print(random_string.lstrip('trs '))

print(random_string.lstrip('s ti'))

website = 'https://www.programiz.com'
print(website.lstrip('htps:/.'))


random_string = ' strthis is good '


# rstrip()
#Removes all trailing whitespace of string.
print(random_string.rstrip())

# Argument doesn't contain space
# No characters are removed.
print(random_string.rstrip('trs'))

print(random_string.lstrip('s ti'))

website = 'https://www.programiz.com/'
print(website.rstrip('htps:/.'))



"""========================================================================="""

#make trance syntex : str.maketrans(dict)
#Returns a translation table to be used in translate function
# example dictionary
dict2 = {"c": "123", "a": "456", "b": "789"}

print(str.maketrans(dict2))

# example dictionary
dict = {97: "123", 98: "456", 99: "789"}

print(str.maketrans(dict))
    
    
"""========================================================================="""

#string.rpartition(separator)
##!/usr/bin/python3

string = "Python is fun is java"

# 'is' separator is found
print(string.rpartition('is '))
print(string.partition('is'))

print(string.rpartition('fun'))
print(string.partition('fun'))

# 'not' separator is not found
print(string.rpartition('not '))
print(string.partition('not '))

string = "Python is fun, isn't it"

# splits at last occurence of 'is'
print(string.rpartition('is'))

"""========================================================================="""


#string.translate(table)

# first string
firstString = "thea "
secondString = "a the"
thirdString = "abi"

string = "abcdgef"
print("Original string:", string)

translation = string.maketrans(firstString, secondString)
print(translation)
# translate string
print("Translated string:", string.translate(translation))


"""========================================================================="""

#syntex : str.rindex(sub, start, end)




"""========================================================================="""

#string.title()
#convert int title format
text = 'My favorite number is 25.'
print(text.title())

text = '234abc k3l2 *43 fun'
print(text.title())


text = "He's an engineer, isn't he?"
print(text.title())



"""========================================================================="""
#zfill  str.zfill(width)
#Returns original string leftpadded with zeros to a total of width characters; intended for numbers, zfill() retains any sign given (less one zero).

text = "fun"
print(text.zfill(15))
print(text.zfill(20))
print(text.zfill(10))


"""========================================================================="""
#format_map(dict)
#formating the strng
i=3
j=2
print("{}is greater then{}{}".format(i,j))

print("{y}{x} is greater then {x}".format(x=3,y=2))

point = {'x':4,'y':-5}
print('{x} {x} aDASDASDASD {x}{y}'.format_map(point))

point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))


#string splitline()
# Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.
grocery = 'Milk\nChicken\rBread\tButter'
print(grocery.splitlines())
print(grocery.splitlines(True))
grocery = 'MilkChicken Bread Butter'
print(grocery.splitlines())

#Find - Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.
g = 'Milk\nChicken\rBread\tButter'
index=g.find("Bread")
index=g.find("not")


#Replace - Replaces all occurrences of old in string with new or at most max occurrences if max given.


g = 'Milk Chicken Bread  Butter bread'
print(g.replace("Bread","B"))

g = 'Milk Chicken Bread Chicken Butter Bread'
print(g.replace("Bread","B"))
exp="2+ 3-5"
print(exp.replace(" ",""))

#Split - Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.

g = 'Milk Chicken Bread Butter Bread'
g.split(" ")
g.split(",")
g.split("Chicken")


#Multiplication with integer============================================
i="hi"*5


#membership operator ==============================================
g = 'Milk Chicken Bread  Butter Bread'
"B" in g

"Bread" not in g



#iterate string through for loop===================================
#using index
for i in range(len(g)):
    print(g[i])

#direct iterate===================================================
for str_val in g:
    print(str_val)

#iterate through while loop========================================
i=0
while(i<len(g)):
    print(g[i])
    i=i+1
    
print(r"hi\thello")

#prin string with r suffix for printing scape char=================
open(r"D:\new\hello.txt")



#convert char to int (ASCII char)

print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))

  






















#expendtabs syntex string.expandtabs(tabsize)

#1
str = 'xyz\t12345\tabc'

# no argument is passed
# default tabsize is 8
result = str.expandtabs()

print(result)


#2
str = "xyz\t12345\tabc"
print('Original String:', str)

# tabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))

# tabsize is set to 3
print('Tabsize 3:', str.expandtabs(3))







