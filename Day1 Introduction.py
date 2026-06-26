Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
22 June 2026

'''
Procedural Language
-------------------
--> This follows step-by-step approach, where code is structure into procedures such as function or routines...
	Eg: C

Object Oriented
---------------
-->This is based on concept of object and classes...
	Eg: python, Java

Python(1991, Guide Van Rossum)
------
1. Dynamically typed language
--> Python knows the type of data we are passing to the variable...

2. Interpreter language
--> Python execute code line-by-line, if any error occur it will stop execution in that line and before lines will gives the ooutput.

3. High_level


Why use python
--------------
--> Easy syntax
--> Cross-platform
--> Wide applications(AI, Ml, Dl,.....)
--> Huge library support


Tokens 
------

1. Keywords
	These are reserved words in python 
	Eg:if, else, for, while,....

2. Identifiers
	Name given to variables, functions, class,...

3. Literals
	89, "Halloo", 4.46,...

4. Operators
	+, -, *, /,...

5. Punctuations
	(), {}, [],...

Rules of variables
------------------

--> Start with A - Z, a - z, _
	Eg: num =1
	    _num = 10
	    Num = 100
--> Do not way to start with Special characters, space, numbers
	Eg: @num = 0
	    n*umm = 12
... 	    1num = 85
... 	    nu12m = 8332
... 	    n u m = 809832
... 	    
... Comments
... --------
... 
... Single line comments --> #
... 	Eg: num = 9
... 	    if num % 2 == 0:  #checking a number is even or odd
... 	    	print("Even")	
...             else:
...             	print("Odd")
... 2. Multi line comments --> '''___''', """___"""
... 
... 
... Boolean
... -------
... 1. True
... 2. False
... Eg:
...     num = 89
...     num_2 = 89
...     print(num == num_2)
... 
... '''
... 
... 
... print(89 + 67)
... num = 89
... num_2 = 67
... total_ = num + num_2
... print(id(num))
... print(id(num_2))
... print(id(total_))
SyntaxError: invalid syntax
>>> 
>>> print(89 + 67)
156
>>> print(id(num))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(id(num))
NameError: name 'num' is not defined. Did you mean: 'sum'?
