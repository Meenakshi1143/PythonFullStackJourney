'''
                                            ERROR HANDLING
                                            --------------


Syntax Error:
-->
Ex:
for j in range(1, 10)
    print(j)
#output: SyntaxError


Indendation Error
-->
Ex:
    num = 10
for j in range(num):
    print(j)
else:
print()
#output: IndendationError

Value Error
-->
num = int(input("Enter a number: ")) #if input given by the user is "ABC", then it shows value error
#output: ValueError


***try:
-->The try block will test the code for error
syntax: try:
            body of the code......

***except:
--> This except block handles the errors in the code
syntax: except:


EXAMPLE
1.
try:
    print(num)
except:
    print("Will get the name error")

2.
try:
    num = int(input("Enter a number: "))
except:
    print("Will get the name error")  #Enter a number: Abcdef     Will get the name error

3.
try:
    num = int(input("Enter a number: "))
except NameError:
    print("Will get the name error") # ValueError
4.

try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(num1 / num2)
    
except ZeroDivisionError:
    print("Will get the Zerodivision error")

except ValueError:
    print("Will get Value Error")

    
***else
--> If the try block does not have any error then the else block will execute
Ex:
try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(num1 / num2)
    
except ZeroDivisionError:
    print("Will get the Zerodivision error")

except ValueError:
    print("Will get Value Error")
else:
    print("No error")
    
***finally



'''


try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(num1 / num2)
    
except ZeroDivisionError:
    print("Will get the Zerodivision Error")

except ValueError:
    print("Will get Value Error")
else:
    print("No Error")
#finally:
print("End")























    


