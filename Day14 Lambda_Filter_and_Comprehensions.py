'''

                                                LAMBDA FUNCTION
                                                ---------------


--> This is also called as annonymous function...
--> A lambda function can take n number of argumrnts but having only one expression

Syntax: lambda arguments : expression
Ex:
some_ = lambda an : an + 12
print(some_ (10))

some_ = lambda an, so : an + so #(Expression should have to be only one)
print(some_(10, 29))

some_ = lambda an, so : an **  so
print(some_(30, 2))

some_ = lambda an, so, why  : an **  so + why
print(some_(10, 2, 100))


***filter() - This is a builtin function use dto filter elments from an iterables such as list, tuple and set based on the condition
--> This is filter() function returns filter object so we can convert that into list, set and tuple

Syntax: filter(function, iterable)
Ex:
nums_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rev_ = filter(lambda a: a % 2 != 0, nums_)
print(list(rev_))

nums_ = [19, 34, 45, 22, 56, 90, 24, 55, 39]
rev_ = filter(lambda a: a % 2 == 0, nums_)
print(tuple(rev_))

nums_ = [19, 34, 45, 22, 56, 90, 24, 55, 39]
rev_ = filter(lambda a: a % 2 == 0, nums_)
sorted_ =  sorted(rev_)
print(sorted_)
#print(tuple(rev_))


                            LIST COMPREHENSION
                            ------------------

--> This offers a shorter syntax when we want to create a new list from the old list
Syntax: var_name = [expression loop condition]
Ex:
#without condition
old_ = [1, 2, 3, 4, 5, 6]
new_= [j for j in old_]
print(new_)


#with condition
old_ = (34, 54, 45, 53, 65, 76)
new_= [j for j in old_ if j % 2 == 0 ]
print(new_)


                            DICTIONARY COMPREHENSION
                            ------------------------
--> This offers a shorter syntax when we want to create a new DICT from the old DICT
Syntax: var_name = [experssion loop]
Ex:
old_dict = {1 : 2, 3 : 4, 5 : 6}
new_dict = {i : j for i, j in old_dict.items()}
print(new_dict)


old_dict = {1 : 2, 3 : 4, 5 : 6, 7 : 3, 8 : 10}
new_dict = {j for i, j in old_dict.items() if j % 2 == 0}
print(new_dict)


'''

old_dict = {1 : 2, 3 : 4, 5 : 6, 7 : 3, 8 : 10}
new_dict = {i : j for i, j in old_dict.items() if j % 2 == 0}
print(type(new_dict))
























