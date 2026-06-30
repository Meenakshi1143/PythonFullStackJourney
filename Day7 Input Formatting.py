'''

                        INPUT FORMATTING FROM USER
                        --------------------------

*** input() - The input() function is used to take input from the user......

1. int
ex:
num1_ = int(input("Enter a number1: "))
num2_ = int(input("Enter a number2: "))
print(num1_ + num2_)


2. string
ex:
str_ = input("Enter a string: ")
print("Good Morning " + str_)

3. float()
ex:
num1_ = float(input("Enter a number1: "))
num2_ = float(input("Enter a number2: "))
print(num1_ + num2_)

3. list
ex:
group_ = list(map(int, input().split()))    # group_ = list(input().split())
print(group_)

4. tuple
ex:
some_ = tuple(map(int, input().split()))
print(some_)

group_ = tuple(input().split())
print(group_)


5. eval
ex:
num = eval(input("Enter: "))
print(type(num))


***string()

1. fstring
ex:
name_ = input("Enter your name: ")
age_ = int(input("Enter your age: "))
print("Hi", name_, "your age is", age_) 
print(f"Hi {name_} your age is {age_}")
print(f"Hi {name_} your age is {age_ + 5}")




'''

name_ = input("Enter your name: ")
age_ = int(input("Enter your age: "))
print("My name is %s and I'm %d years old....." %(name_, age_))


















