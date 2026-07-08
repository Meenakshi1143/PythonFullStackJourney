'''
                                    FUNCTIONS
                                    ---------
--> Function is a block of codethat can be reusable
--> FUnction can avoid teh repeated line of code...
Functions of 2 types
--------------------
1. built-in
--> Ex: print(), max(), type(),min(), sum().....

2. user-define
--> this function starts with keyword def
syntax:
def func_name(parameters):
    ------------
    ----------
    ---
func_name(arguments)
ex:
def add(a, b):
    print(a + b)
add(3,4)

def func():
    print("Hellooooo!!!!")
func()
    

TYPES OF ARGUMENTS
------------------
1. Required arguments - we have to pass same number of arguments with definition of the function
ex:
def add(num1, num2):
    print(num1 + num2)
add(4,6)

def add(num1, num2):
    print(num1)
#add(42,43)
add(43)

2. Default arguments
Ex:
def add(a,b):
    print(a)
    print(a + b)
add( b = "Good Morning....", a = "helloo ")


a = 10
b =4
c = 9
def add(num1, num2, num3):
    print(num1)
    print(num2)
    print(num3)
    print(num1 + num2 + num3)
add(a, b, c)



3. Keyword arguments - we can pass as a pair like (variabe = datatype)
Ex:
def add(a,b):
    print(a + b)
add(a = "helloo ", b = "Good Morning....")


4. Variable length arguments - can pass n number of arguments and just using args in the parameters, will receive tuple of arguments
Ex:
#using single star (*args)
num1 = 34
num2 = 4
num3 = 43
num4 = 5
def add(*a):
    print(a, a[0], a[3], sep = '\n')
add(num1, num2, num3, num4)

#using double star(**args)
def all_ (**Any):
    print(Any)
all_(Nmae = "Meenakshi", Age = 21)


def all_ (**Any):
    print(Any, Any.keys(), Any['Age'], sep = '\n')
all_(Name = "Meenakshi", Age = 21)

NOTE
----
--> to change the global variable by using keyword (global) that can be changed completly  inside and outsideof function..

****Global Variable
Ex:
num = 32
def func_():
    print(num)
func_(num)

#example
num = 92
def func_():
    global num
    num = 32
    print(num)
func_()
print(num)

**** Local Variable
Ex:
#num = 92
def func_():
    num = 32
    print(num)
func_()
print(num)
'''

num = 92
def func_():
    global num
    num = 32
    print(num)
func_()
print(num)
    
