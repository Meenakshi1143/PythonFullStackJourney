'''
29 April 2026
                     TYPE CONVERSIONS
                     ----------------
--> this is used converting  one datatype to another....

INT --> String, Float
    ex:
    num_ = 89
    num2_ = float(num_)
    print(num2_)
    print(type(num_))
    so = str(num_)
    print(type(so))

FLOAT --> String, Integer
    ex:
    num_ = 8.9
    num2_ = str(num_)
    print(num2_)
    print(type(num2_))
    so = int(num_)
    print(so)

STRING --> Integers, Float, List, Tuple
    ex:
    # string - integers
    num = "78"
    num_ = int(num)
    print(num_ + 10)

    #cstring - float
    float_ = "67.89"
    num2_ = float(float_)
    print(num2_ + num_)

    # string - list
    str_ = "PYTHON"
    num_ = "123456"
    convert_ = list(str_)
    print(convert_)
    # string -tuple
    convert1_ = tuple(str_)
    print(convert_)

LIST --> String, Tuple, Dictionary
    ex:
    # list - string
    var_ = ["P", "Y", "T", "H", "O", "N"]
    Con_ = str(var_)
    print(Con_)
    con1_ = "".join(var_)
    print(con1_)

    # list - tuple
    var_ = ["P", "Y", "T", "H", "O", "N"]
    Con_ = tuple(var_)
    print(Con_)

    # list - dictionary
    list_ = [("a", 11), ("b", 22)]
    con_ = dict(list_)
    print(con_)


TUPLE : String, Lists
    ex:
    


built-in functions
------------------
str()
float()
int()
list()
dict()


'''

coins = (1, 2, 5, 10, 20)
print(list(coins))

letters = ('a', 'b', 'c', 'd', 'e')
convert1_ = "".join(letters)
print(convert1_)


