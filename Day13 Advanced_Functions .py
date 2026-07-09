'''

Passing by value
----------------
Ex:

def some(a):
    print(a)

some(10)


def some(a):
    for j in a:
        print(j)

some([1, 2, 3])


def some(a):
    for j in a:
        print(j)

some((10, 20, 30 ,40))

Pass by reffernce
-----------------
a = [1, 2, 3, 4]
def some(a):
    print(a)

some(a)

return Ketyword
---------------
--> In a function if a return is executed then it will be exit from the function with certain returned values
Ex:
def func_(b):
    return 5 + b
a = func_(10)
c = func_(100)
print(a)
print(c)



#code for list of builtin_functions
import builtins

builtin_functions = [
    name for name in dir(builtins)
    if callable(getattr(builtins, name))]
print(builtin_functions)
print(f"Total built-in functions are {len(builtin_functions)}")


                                    RECURSIVE FUNCTION
                                    ------------------
--> Recursive fnction that calls itself repeatedly untill a specified condition it met...
Syntax:
def func_name(parameter):
    if condition: #base case
        return statement
    else:
        return statement
print(func_name(agruments))

Example:

def func_name(num):
    if num == 1:
        return 1
    else:
        return num * func_name(num - 1)
num = int(input())
print(func_name(num))

def func_name(num):
    if num == 1:
        print(num)
        return 1
    else:
        print(num, "*", end = " ")
        return num * func_name(num - 1)  #5 * (4 * (3 * (2 * (1))))
num = int(input())
print(func_name(num))

    
'''



def func_name(num):
    if num == 1:
        print(num)
        return 1
    else:
        print(num, "*", end = " ")
        return num * func_name(num - 1)  #5 * (4 * (3 * (2 * (1))))
num = int(input())
print(func_name(num))

















    
