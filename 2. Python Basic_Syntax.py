# -*- coding: utf-8 -*-

"""
Python Identifiers
A Python identifier is a name used to identify a variable, function, class, module or other object. An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9).

Python does not allow punctuation characters such as @, $, and % within identifiers. Python is a case sensitive programming language. Thus, Manpower and manpower are two different identifiers in Python.

Here are naming conventions for Python identifiers −

Class names start with an uppercase letter. All other identifiers start with a lowercase letter.

Starting an identifier with a single leading underscore indicates that the identifier is private.

Starting an identifier with two leading underscores indicates a strong private identifier.

If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.
"""
I=0     #ok
i=9     #ok
9i=0    # not ok
i9=0    #ok
i9i=0   #ok
@i=0    #ok
i@=4    #ok
i@i     #ok
__i__=0 #ok
_9=0my  #ok
my_name="ram" #ok
_i=0          #ok
__i=0         #ok
__i__=0       #OK

"""
Reserved Words
The following list shows the Python keywords. These are reserved words and you cannot use them as constants or variables or any other identifier names. All the Python keywords contain lowercase letters only.

and	    exec	    not
as	    finally  	or
assert	for     	pass
break	from	    print
class	global   	raise
continue if	        return
def	    import	    try
del	    in	        while
elif	is	        with
else	lambda	    yield
except
""" 		

"""
Multiline statment
"""
i=1+2+3\
  +4+5\
  +7+8



#paragraph 
i="""with the 
triple quote you can write 
write a paragraph
and can stroe in a variable."""

#Variable Assignmnt

h='k'
h=chr('k')
i=2+5j
i=5j
i=True
i=False


#multiple variable assignment in a single line .
i,j,k=1,2.0,"hello"
a=b=c=1

#delete a variable
del i,j,k


#comment in python
#1. Single Line Comment using '#' symbol
#2. Multiline Comment Using  """ triple Quote


# this is a single line Comment
"""
this is a
Multiline 
Comment
"""

"""  
Indentation
Python does not use braces({}) to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line indentation, which is rigidly enforced.

The number of spaces in the indentation is variable, but all statements within the block must be indented the same amount. For example −
"""
if True:
   print ("True")

else:
   print ("False")

#However, the following block generates an error −

if True:
   print ("Answer")
   print ("True")

else:
   print "(Answer")
   print ("False")
   
#Thus, in Python all the continuous lines indented with the same number of spaces would form a block. The following example has various statement blocks −

"""
Using Blank Lines
A line containing only whitespace, possibly with a comment, is known as a blank line and Python totally ignores it.

In an interactive interpreter session, you must enter an empty physical line to terminate a multiline statement.

Waiting for the User
The following line of the program displays the prompt and, the statement saying “Press the enter key to exit”, and then waits for the user to take action −
"""


input("\n\nPress the enter key to exit.")
#Here, "\n\n" is used to create two new lines before displaying the actual line. Once the user presses the key, the program ends. This is a nice trick to keep a console window open until the user is done with an application.


"""
Multiple Statements on a Single Line
The semicolon ( ; ) allows multiple statements on a single line given that no statement starts a new code block. Here is a sample snip using the semicolon −
"""
import sys; x = 'foo'; sys.stdout.write(x + '\n')


"""
Multiple Statement Groups as Suites
Groups of individual statements, which make a single code block are called suites in Python. Compound or complex statements, such as if, while, def, and class require a header line and a suite.

Header lines begin the statement (with the keyword) and terminate with a colon ( : ) and are followed by one or more lines which make up the suite. For example −
"""
if expression : 
   suite
elif expression : 
   suite 
else : 
   suite
   
   
"""
Command Line Arguments
Many programs can be run to provide you with some basic information about how they should be run. Python enables you to do this with -h −

$ python -h
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):
-c cmd : program passed in as string (terminates option list)
-d     : debug output from parser (also PYTHONDEBUG=x)
-E     : ignore environment variables (such as PYTHONPATH)
-h     : print this help message and exit

[ etc. ]
You can also program your script in such a way that it should accept various options. Command Line Arguments is an advanced topic. Let us understand it.
"""

