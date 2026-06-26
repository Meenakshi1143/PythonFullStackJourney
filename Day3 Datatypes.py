'''
24 April 2026

               Datatypes
               ---------

int --> num = 218

float --> num1 = 33.3
print(7.89 // 6.89)

Strings
-------
--> String is sequence of character teht are enclosed in ' ', " ", """ """
--> sting is immutable

Concatination( + )
------------------
--> here , the (+) operator act as to concatinate 
so = "Codegnan "
any = "institution"
print(so + any)

INDEXING
--------
--> This is used to access the particular char in the string by pass index position value....
--> Index start from 0..
--> We have negative indexing to count position from last to first...

str = "My self Meenakshi"
print(str[8])
print(str[-7])
print(str[5 : -7])

METHODS
-------

1. replace()
--> This method is used to change any substring in that particular string...
    syntax--> variable_name.replace("old_string", "new_string",  
ex:
str = "My self Meenakshi"
print(str.replace("self", "name is"))       #My name is Meenakshi
print(str)                                  #My self Meenakshi
print(str.replace("e", "E"))                #My sElf MEEnakshi
print(str.replace("e", "E", 2))             #My sElf MEEnakshi
 
2. join()
--> This method used to add a new substring after each character in string...
    syntax: "string".join(variable_name)
    ex:
        str = "My self Meenakshi"
        print("*".join(str))     # M*y* *s*e*l*f* *M*e*e*n*a*k*s*h*i

3. split()
--> This method can divide the string into diff index into list, based on ths string pass by us.....
    syntax: variableName.split("substring
    ex:
        str = "My self Meenakshi"
        print(str.split(" "))   # ['My', 'self', 'Meenakshi']
        print(str.split(" self"))    #['My', ' Meenakshi']

        
4. count()
--> Used to count the substring in the particular string and also specify the index position
    syntax:  variablename.count("substring", starting_index_position, ending_index))

    ex:
    str = "My self Meenakshi"
    print(str.count("e"))    #3


*** STRING BUILT-IN FUNCTION
----------------------------

1. len()--> This will find length of characters present in that string
    ex:
    str = "My self Meenakshi"
    print(len(str))    #17
    print(len("self")) #4

2. min()
    ex:
        str = "My self Meenakshi"
        print(min("self"))  #e
        print(min(str))     # (space will be the minimum  character)

'''

str = "My self Meenakshi"
print(min(str))
