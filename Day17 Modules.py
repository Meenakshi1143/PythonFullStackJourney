'''
                                                MODULES
                                                -------

--> A Module is a python file (.py) that contains reusable code

1. Variables
2. FUnctions
3. Classes
4. Objects
5. Statements

Why this
--------
--> Instead of writing the same code reaptedly, we can store it in a module and us whenever needed.

Types of Modules
----------------
1. User-define
import first_module
print(first_module.add(17,13))
print(first_module.sub(17,13))
print(first_module.mul(17,13))
print(first_module.div(17,13))

import specific functions
-------------------------
from first_module import add,sub
print(add(17,13))
print(sub(17,13))

from first_module import*
from first_module import *
print(floor_division(17, 10))
print(power(2, 3))
print(remainder(3, 2))
print(add(2, 3))
print(sub(67, 32))

Using alias name
----------------
import first_module as m
print(m. add(12,9))

import first_module as m
print(m. add(12,9))
print(m. mul(12,9))


2. Built-in
-----------
** math
Ex:
import math
print(math.sqrt(25)) # sqrt() - square root
print(math.factorial(5)) # factorial() - factorial
print(math.pow(2, 5)) #pow() - power
print(math.pi) # pi - pi value
# ceil() - roundup

**os
--> The os module is used to interact with operating system
Ex:
import os
print(os.getcwd())       
os.mkdir()
OS FUNCTIONS
------------
getcwd() - current directory   
mkdir() - create folder
rmdir() - remove folder


**sys
--> This will provide the information about the python interpeter'

import sys
print(sys.version)

**random
--> Used to generate random values

import random
print(random.randint(1000, 9999))
colors = ['Red', 'Green', 'Blue', 'Pink', 'Black']
print(random.choice(colors))
'''
import random
colors = ['Red', 'Green', 'Blue', 'Pink', 'Black']
print(random.choice(colors))
