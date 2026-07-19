'''
                                POLYMORPHISM

--> Polymorphism means many forms
--> It allows same method, function or operator to perform different tasks depending on the same object....

Types:
1. Method Overloading:
--> Method Overloading means having multiple methods with the same name but different parameters
Ex:
class calculator:
    def add(self, num1_, num2_ = 0):
        print(num1_ + num2_)
    def add(self, num1_,num2_, num3_  = 0):
        print(num1_ + num2_ + num3_)
obj_ = calculator()
obj_.add(4, 12)
obj_.add(4, 12, 10)


2. Method Overriding:
--> The method overriding occurs when a child class provides its own implementation of a method already defined in its parent class.
Ex:
class animals:
    def sound(self):
        print("Animals make sounds")
class dog(animals):
    def sound(self):
        print("Dogs bark")
obj_ = dog()
obj_.sound()

class calculator:
    def add(self, num1_, num2_ = 0):
        print(num1_ + num2_)
class cal_(calculator):
    def add(self, num1_,num2_, num3_  = 0):
        print(num1_ + num2_ + num3_)
obj_ = cal_()
obj_.add(4, 12)
obj_.add(4, 12, 10)

3. Operator Overloading
--> This allows operators (+, -, *) to work differently for user-defined objects
1) __add__ (+)
2) __sub__ (-)
3) __mul__ (*)
4) __truediv__  (/)
5) __eq__ (==)
6) __It__ (<)

Ex:
class student:
    def __init__(self, marks):
        self.marks = marks
    def __add__(self, other):
        return self.marks - other.marks
s1 = student(78)
s2 = student(12)
print(s1 + s2)



class student:
    def __init__(self, marks):
        self.marks = marks
    def __sub__(self, other):
        return self.marks * other.marks
s1 = student(23)
s2 = student(2)
print(s1 - s2)
                                                                                                                                                                                                                                                                                                            
                                            DATA ABSTRACTION

--> Data abstraction is the process of hiding implemented details on showing only the essential data to the user.

Ex:
-ATM
-Car
-Apps


from abc import ABC, abstractmethod
class parent:
    @abstractmethod
    def display(self):
        pass

'''
from abc import ABC, abstractmethod
class bank:
    @abstractmethod
    def interest(self):
        raise NotImplementedError('SubClass must implemented interest()')

class SBI(bank):
    def interest(self):
        print('SBI interest Rate: 4.5%')
class HDFC(bank):
    def interest(self):
        print('HDFC interest Rate: 8.7%')        
class ICICI(bank):
    def interest(self):
        print('ICICI interest Rate: 5.9%')
banks = [SBI(), HDFC(), ICICI()]
for j in banks:
    j.interest()


























