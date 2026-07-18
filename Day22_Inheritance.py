'''
                                            INHERITANCE
                                            -----------

--> Inheritance is an OOP concept where one class(child/derived) acquired the properties and methods of another class(Parent/Base)


class parent:
    pass
class child(parent):
    pass


Types of Inheitance
-------------------
1. Single Inheritance:
--> A child class inherits from one parent is Single inheritance.
Ex:
class animal:
    def sound(self):
        print("Animals make sound")
class dog(animal):
    def barks(self):
        print("Dog Barks")

d = dog()
d.sound()
d.barks()

class father:
    def land(self):
        print("5'acr of land")
class son(father):
    def flat(self):
        print("3BHK flat")
s = son()
s.land()
s.flat()



2. Multiple Inheritance
--> A  child class inherits more than one parent is called Multiple inheritance
Ex:
class father:
    def skills(self):
        print("Driving")
class mother:
    def talent(self):
        print("Cooking")
class brother:
    def learn(self):
        print("study")
class son(father, mother, brother):
    def mine(self):
        print("Sleeping")
all_ = son()
all_.skills()
all_.talent()
all_.learn()
all_.mine()


3. Multi-level Inheritance
--> One child class becomes the parent for another class
Ex:
class grandFather:
    def house(self):
        print("Own House")
class father(grandFather):
    def flat(self):
        print("New 3BHK flat")
class son(father):
    def car(self):
        print("Have a car")
fam_ = son()
fam_.house()
fam_.flat()
fam_.car()


4. Hierarchical Inheritance
--> Multiple childs inherits from the same parent
Ex:
class mother:
    def gold(self):
        print("10kgs Gold")
class anki(mother):
    def show1_(self):
        print("Will get 5Kg Gold")
class moni(mother):
    def show2_(self):
        print("Will get remaining 5kg Gold")
child1_= anki()
child2_ = moni()

child1_. gold()
child1_.show1_()

child2_. gold()
child2_.show2_()


class animal:
    def sounds(self):
        print("Animals makes sounds")
class dog(animal):
    def bark(self):
        print("Dogs are Barking")
class cat(animal):
    def meow(self):
        print("cats make ssound as Meow Meow")
a1_= dog()
a2_ = cat()

a1_. sounds()
a1_.bark()

a2_. sounds()
a2_.meow()


5. Hybrid Inheritance
--> This is the combination of two or more types of inheritance
--> Example multiple + multi-level

Ex:
class A:
    def methodA(self):
        print("Class A")
class B(A):
    def methodB(self):
        print("Class B")
class C(A):
    def methodC(self):
        print("Class C")
class D(B, C):
    def methodD(self):
        print("Class D")

so_ = D()
so_.methodA()
so_.methodB()
so_.methodC()
so_.methodD()



super() function
----------------
--> This super() function  is used to access the parent class methods or constructor in the child class....
Ex:
#Using Method
class parent:
    def show(self):
        print("Parent Method")
class child(parent):
    def show(self):
        super().show()
        print("Child class")
child_ = child()
child_.show()

#Using Constructor
class person:
    def __init__(self, name):
        self.name = name
class student(person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
    def display(self):
        print(self.name)
        print(self.roll)
an = student("Meenakshi", 446)
an.display()


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class student(person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll
    def display(self):
        print("Student Details: ")
        print(self.name, self.age, self.roll)
class faculty(person):
    def __init__(self, name, age, fID):
        super().__init__(name, age)
        self.fID = fID
    def display(self):
        print("\nFaculty Details: ")
        print(self.name, self.age, self.fID)
        
an = student("V.Meenakshi", 21, 446)
an1 = faculty("Dr.G.Sharmila", 65, "AU012")
an.display()
an1.display()

'''


class person:
    def __init__(self, name, age):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
class student(person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = int(input("Roll No. "))
    def display(self):
        print("Student Details: ")
        print(self.name, self.age, self.roll)
class faculty(person):
    def __init__(self, name, age, fID):
        super().__init__(name, age)
        self.fID = fID
    def display(self):
        print("\nFaculty Details: ")
        print(self.name, self.age, self.fID)
        
an = student(name, age, roll)
an1 = faculty("Dr.G.Sharmila", 65, "AU012")
an.display()
an1.display()








    

