# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:46:49 2018

@author: james
"""
"""
A regular expression is a special sequence of characters that 
helps you match or find other strings or sets of strings, using a 
specialized syntax held in a pattern. Regular expressions are widely
 used in UNIX world.

The module re provides full support for Perl-like regular 
expressions in Python. The re module raises the exception 
re.error if an error occurs while compiling or using a regular
expression.

We would cover two important functions, which would be used to
handle regular expressions. Nevertheless, a small thing 
first: There are various characters, which would have special 
meaning when they are used in regular expression. To avoid any
confusion while dealing with regular expressions, we would use Raw
Strings as r'expression'.
"""

"""
by reg exp we do mainly these things:
1. match pattern
2. search pattern
3. Findall pattern
4. replace pattern
"""

import re

#Basic Patterns: Ordinary Characters
#1. match==========================================
pattern = r"Cookie"
sequence = r"a Cookie is ok"
if re.match(pattern, sequence):
  print("Match!")
else: 
    print("Not a match!")
    
#2. Search=========================================
re.search(pattern, sequence)
#==================================================
re.search(r'C.....e', 'Cookie')

pattern = r"Cookie"
sequence = r"a Cookie is Cookie ok"
print("Match!",re.search(pattern, sequence))


#3.findall===========================================
print("findall!",re.findall(pattern, sequence))

#=================================================
re.findall(r'.ut', 'cut put put cut rut euu')


#Match ,search or find all by regular expression

#we have many regular expreson symbole to find patern let see one by one.
"""
1  "."

Match any character except newline
"""

print(re.findall(r'Co.k.e', 'Coikee Coekge'))


"""===============================================
2.	
\d find integer in string
"""
print(re.search(r'\d', 'a123 ghj23 23'))
#++++++++++++++++++++++++++++++++++++++++++++++++++
print(re.match(r'\d', '223 ghj'))
#++++++++++++++++++++++++++++++++++++++++++++++++++
print(re.findall(r'\d\d\d', '123 ghj234 33')) #find combination of three digits
#+++++++++++++++++++++++++++++++++++++++++++++++++++
print(re.findall(r'\d\d\d', '123 ghj'))

#you can do this also by {}+++++++++++++++++++++++++
print(re.search(r'\d{1}', '123 ghj')) 
#++++++++++++++++++++++++++++++++++++++++++++++++++++
print(re.match(r'\d{2}', '123 ghj'))
#find tow or four digit only++++++++++++++++++++++++++++++++
print(re.findall(r'\d{2,4}', '1233 ghj123'))
#++++++++++++++++++++++++++++++++++++++++++++++++++++
print(re.search(r'\d{2,3}', '123 5 ghj'))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
print(re.match(r'\d{1,3}', '123 3ghj'))
#++++++++++++++++++++++++++++++++++++++++++++++++++++
print(re.findall(r'\d{1,3}', '123 2ghj'))


"""==================================================
Match a digit: [0-9]

"""
print(re.findall(r'[0-9]', '123 2ghj'))



"""==============================================
3	
\D
Match a nondigit: [^0-9]
"""

print(re.search(r'\D', 'as 123 ghj asdf'))
print(re.match(r'\D', 'abc 123 ghj'))
print(re.findall(r'\D', 'ab 123 ghj'))


print(re.search(r'\D{3}', '123 ghj asd'))
print(re.match(r'\D{2}', 'aaa 123 ghjasd'))
print(re.findall(r'\D{2}', '123 ghj'))

print(re.search(r'\D{1,3}', '123 5ghj'))
print(re.match(r'\D{1,3}', '123 3ghj'))
print(re.findall(r'\D{1,3}', '123 2ghj'))


"""================================================
4	
\s
Match a whitespace character: [ \t\r\n\f ' ']
"""
print(re.search(r'\s', 'as 123 ghj asdf\t'))
print(re.match(r'\s', ' abc 123 ghj'))
print(re.findall(r'\s', 'ab 123 ghj\t'))

"""=================================================
5	
\S
Match nonwhitespace: [^ \t\r\n\f' ']
"""
print(re.search(r'\S', 'as 123 ghj asdf\t'))
print(re.match(r'\S', ' abc 123 ghj'))
print(re.findall(r'\S', 'ab 123 ghj\t'))

"""===================================================
6	
\w

Match a single word character: [A-Za-z0-9_]
"""
print(re.search(r'\w\w\w', 'as 123 ghj asdf\t'))
print(re.match(r'\w\w\w', 'abc 123 ghj'))
print(re.findall(r'\w', 'ab 1233 ghj\t'))


"""====================================================
7	
\W
Match a nonword character: [^A-Za-z0-9_]
"""
print(re.search(r'\W', 'as 123 ghj asdf@'))
print(re.match(r'\W', 'abc 123 ghj'))
print(re.findall(r'\W', 'ab 123 ghj@'))



"""======================================================
8 [Pp]ython"
Match optional charecter either or
"""

print(re.findall(r'[pP]ython', 'python Pythonis awesome.'))

"""======================================================

9 [aeiou]
Match any of this character
"""
print(re.findall(r'[aeiou]', 'ab 123 abi ghj@'))


"""========================================================
10 [0-9]
Match any digit; same as [0123456789]
"""
print(re.findall(r'[0-9]', 'ab 123abc abi ghj@'))

"""========================================================
5	[a-z]
Match any lowercase ASCII letter
"""
"""======================================================
6  
[A-Z]
Match any uppercase ASCII letter
"""

"""=========================================================
7	[a-zA-Z0-9]
Match b/w a to z , A to Z, 0 to 9 any of the above
"""
print(re.findall(r'[^a-zA-Z0-9]', 'ab 123abc abi ghj@'))

"""=========================================================
8	
[^aeiou]
Match anything other than a lowercase vowel
"""

"""=========================================================
9	
[^0-9]

Match anything other than a digit
"""                                

"""========================================================
*  match 0 or more occurence
+  match atleast one or more than one
"""
print(re.findall(r'10+1', '1000000000011111000011000101000010'))
print(re.findall(r'10+1', '1000000000011111000011000101000010'))


"""========================================================
^Python start with P
\Python Start with P
Python$   end with P
Python\Z  end with P
"""

re.findall(r'^Python', ' Python is awesome Pern is also')
re.findall(r'\APython', 'Python is awesome Pern is also')
re.findall(r'Python$', 'Python is awesome Pern is also Python')

#Match "Python" at the start of a string or internal line

print(re.findall(r'10*1', '100000000001111100001100001000010'))
print(re.findall(r'1.*1', '10000000001100001100001000010'))

re.findall(r'P[a-z]*n', 'Python is awesome Pern is also')


"""=====================================================
Python$

Match "Python" at the end of a string or line
"""
"""======================================================
\APython
Match "Python" at the bigning of a string or line
"""

"""======================================================
\bPython\b
Match at a word boundary
"""
re.findall(r'\bPython\b', 'aPython is Python awesome Python is also Python')
re.findall(r'Python\b', 'is Python awesome Pern is alsoPython is good')

#above Match "Python" at a word boundary

"""	======================================================
\brub\B
\B is nonword boundary: match "rub" in "rube" and "ruby" but not alone
"""
re.findall(r'\bPython\B', 'is Pythonawesome is also')


"""=======================================================
Python(?=!)
Match "Python", if followed by an exclamation point.
"""
re.findall(r'Python(?=!)', 'is Python! python awesome is also')
re.findall(r'Python(?=a)', 'is Pythona awesome is also')



"""=======================================================
()
Return only the patter mathched
"""
re.findall(r'pyth(on)', 'is python python on awesome is also')
#it will return only on

"""=======================================================	
Python(?!a)
Match "Python", if not followed by an exclamation point.
"""
re.findall(r'Python(?!!)', 'is Python!  Python awesome is also')
re.findall(r'Python(?!a)', 'is Python Pythona awesome is also')



"""========================================================
Matching Versus Searching
Python offers two different primitive operations based on regular 
expressions: match checks for a match only at the beginning of the 
string, while search checks for a match anywhere in the string
 (this is what Perl does by default).
"""
#eg
import re
line = """Cats are smarter than dogs 
          dogs""";

matchObj = re.match( r'dogs', line, re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

searchObj = re.search( r'dogs', line, re.I)
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
else:
   print ("Nothing found!!")
   



#Group Search==================================================
import re

line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*)', line, re.I)

if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))

else:
   print ("Nothing found!!")

   
   

"""
Search and Replace

Syntax
re.sub(pattern, repl, string, max=0)

This method replaces all occurrences of the RE pattern in string with repl,
substituting all occurrences unless max is provided.
This method returns modified string.
"""
#eg.
import re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print ("Phone Num : ", num)




"""=====================================================
Repetition Cases

1. ruby?
Match "rub" or "ruby": the y is optional
"""
re.findall(r'ruby?', 'ruby is awesome and rub is also')

"""
2.ruby*================================================

Match "rub" plus 0 or more ys
"""
re.findall(r'ruby*', 'rubyyyy is awesome and rub is also')


"""	=====================================================
ruby+

Match "ruby" plus 1 or more y
"""
re.findall(r'ruby+', 'rubyyy is awesome and rub is also')

"""======================================================
\d{3,}
Match 3 or more digits
"""
re.findall(r'\d{3,}', 'ruby is awesome and rub is also 11 122 1333 144444')




"""=========================================================
Alternatives

#1	
python|perl

Match "python" or "perl"
"""
re.findall("python|perl","python perl")


"""==========================================================
2	
rub[y|le]

Match "ruby" or "ruble"
"""
re.findall("rub[y|le]","ruby rube ruble")


"""===========================================================
3
Python[!+|a?]
"Python" followed by one or more ! or one a
"""

re.findall("Python[!+|a?]*","Python! Python Pythona")

   
"""==================================================================
R(?#comment)
  
Matches "R". All the rest is a comment
"""
re.search("(.*)ok R(?#comment)","ok Rok R#co")



"""=================================================================
rub(?:y|le))
"""
re.findall("Rub[?i:y|le]","Ruby RUBy Rube Rubl")

"""==================================================================
search ()  in string
"""
re.findall(" [(].*[)]","pytob (pyton)pp")
re.findall(" \(.*\)","pytob (pyton)pp")
re.findall(" \(.*\)","pytob (pyton)pp")

"""=================================================================
search \  in string
"""
re.findall(r"[\\].*[\\]","pytob \pyton\perl")


"""=================================================================
find  '' in string
"""
re.findall(" '.*'","pytob 'pyton'pp")

"""=================================================================
find "  in a string
"""
re.findall(" \".*\"","pytob \"pyton\"pp")







