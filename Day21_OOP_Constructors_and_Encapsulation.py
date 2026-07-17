'''
self keyword:
--> Self refers to current object
Ex:
class Test:
    def display(self):
        print(self)
t = Test()
print(t)
t.display()

Constructor:
--> This constructor initilizes mthe object automatically when it is created 
Ex:
class Batchs:

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def display(self):
        print("Name :", self.name)
        print("Branch :", self.branch)

obj = Batchs("Meenakshi", "CSE")
obj.display()

Access Specifiers
-----------------
1. Public
Ex:
class Batchs:

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def display(self):
        print("Name :", self.name)
        print("Branch :", self.branch)


b = Batchs("Meenakshi", "CSE")
b.display()

2. Protected:
Ex:
class fam():
    def __init__(self):
        self._name = 'Meenakshi'
f = fam()
print(f._name)

3. Private:
Ex:
class bank:
    def __init__(self):
        self.__pin = '2034'
ac = bank()
print(ac._bank__pin)


class bank:
    def __init__(self):
        self.__pin = '2034'
    def display():
        print(self.__pin)
ac = bank()
print(ac._bank__pin)

***Ecapsulation:
--> Wrapping the data and methods into single unit(class) while controlling access to data
Ex:
class atm:
    def __init__(self, balance):
        self._balance = balance
    def deposit(self, amount):
        self._balance += amount
        print(self._balance)
t = atm(balance=int(input("Enter amount ")))
t.deposit(amount=int(input("Enter amount ")))
        

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def dis(self):
       print(f"Your Name is {self.name} your {self.age} years old")

s1 = Student(name = input("Enter your name: "), age = input("Enter your age: "))
s1.dis()
'''
class details:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1 = details("Raju",21)
s2 = details("Rani",31)
print(s1.age)
print(s2.age)
if s1.age == s2.age:
    print("Equal ages")
else:
    print("Not equal")
