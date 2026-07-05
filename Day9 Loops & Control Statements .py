'''
                    LOOPS
                    -----

1. for loop - a for loop is used to iterate over a sequence, list, tuple, dictionary

ex:
# using String
any_ = "PYTHON IS A LANGUAGE"
for i in any_:
    print(i)

# using tuple
any1_ = (1, 2, 3, 4, 5, 6, 'a', 'b', 'c')
for i in any1_: 
    print(i)
    
# using list
any1_ = [1, 2, "abcd", 3, 4]
for i in any1_:    # i is an instance variable
    print(i)
    
# using Dictionaries
any1_ = {
    "Name" : "Meenakshi",
    "Age" : 21,
    "Section" : "A9 CSE-7"
    }
for i in any1_.items():
    print(i)

else in for loop
----------------
--> the else block will be executed after the for loop, but incase the loop is breaked then it will never enter into else block
Ex:
#without brak
list_ = [1, 2, 3, 4, 5]
for val in list_:
    print(val)
else:
    print("Entered")

#with break
list_ = [1, 2, 3, 4, 5]
for val in list_:
    print(val)
    if val == 3:
        break
else:
    print("Entered")

    
2. while loop - this will be executed untill the condition becomes true....
Ex:
i = 1
while i < 5:
    print(i)
    i =+ 1

                            CONTROL STATEMENTS
                            ------------------

1. break - this is used to exit from the  loop
Ex:
list_ = [1, 2, 3, 4, 5]
for val in list_:
    print(val)
    
else:
    print("Entered")
    
2. continue - this will skip the current iteration
Ex:
list_ = [1, 2, 3, 4, 5, 6, 7, 8]
for val in list_:
    if val == 7:
        continue
    print(val)
else:
    print("Entered")

3. pass - spacce holder

range() - this is a in-built function that is useed to generate a sequence upto limit
syntax : range(start, end, step)
Ex:
n = int(input())
for i in range(1, n + 1, 2):
    print(i)

** assert keyword - it will check the condition , but it will raise an error incase it is false....
Ex:
num = 10
assert num > -10, "must be negative"
'''

num = int(input("Enter your age: "))
assert num >= 18, "You must 18 years old.."


