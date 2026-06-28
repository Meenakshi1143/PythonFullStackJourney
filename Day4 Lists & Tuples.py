'''
                   LIST DATATYPE 
                   -------------
LIST --> This is a collection of differnet datatypes that are enclosed in [] seperated by commas(,)
        all_type = [1, 'Python', [1,2]]
        print(all_type)

     -->List is muttable

LIST METHODS
------------
1. append() - This is used to add new item into list , but it will add in the last index position
    ex:
    any_ = [1, 2, 3, 4]
    print(any_)
    any_.append(5)
    print(any_)
    any_.append(6)
    print(any_)
    any_.append("python")
    print(any_)
    
2. extend() - this is also add a item in the last index position, but it will give each valu in the each index position
            - it will be assigned based on index
    ex:
    any_ = [1, 2, 3, 4]
    print(any_)
    any_.extend([5,6])
    print(any_)                    #[1, 2, 3, 4, 5, 6]
    any_.extend('PYTHON')
    print(any_)                    #[1, 2, 3, 4, 5, 6, 'P', 'Y', 'T', 'H', 'O', 'N']

    
3. pop()- USED TO DELETE THE VALUE FROM THE LIST, BUT IT WILL DELETE BASED ON INDEX POSITION
    syntax --> variable_name.pop(index position)
    EX:
    any_ = [1, 2, 45, 78, 23, 90]
    any_.pop(1)
    print(any_)                #[1, 45, 78, 23, 90]

    
4. remove() - used to delete the item from the list, but it will delete direct value from index 
    syntax --> variable_name.pop(value)
    ex:
    any_ = [1, 2, 45, 78, 23, 90]
    any_.remove(1)
    print(any_)                 #[2, 45, 78, 23, 90]

    
5. insert()


    MUTTABLE                            IMMUTABLE
    --------                            ---------
    1. The data can be modified(list)   can't be modified(string)
    ex:                                 ex:
    any_ = [1, 2, 3, 4]                 str = "My self Meenakshi"
    print(any_)                         print(str.replace("self", "name is"))
    any_.append(5)                      print(str)                   
    print(any_)                         print(str.replace("e", "E")) 
    any_.append(6)                      print(str.replace("e", "E", 2))  
    print(any_)

INDEXING
--------
EX:
any_ = [1, 2, 'python is a language',[45, 78, "java is a language", [1,23], 90], 'hello']
print(any_[3])                     #[45, 78, 'java is a language', [1, 23], 90]
print(any_[3][2])                  #java is a language
print(any_[3][2][10])              #1
print(any_[3][3][1])               #23


                          TUPLE
                          -----
Tuple --> This is a collection of differnet datatypes that are enclosed in () seperated by commas(,)
      --> it is immutable
ex:

how_ = (1, 2, 3, 4, 'python', [4, 5], (90, 78))
print(how_)                     #(1, 2, 3, 4, 'python', [4, 5], (90, 78))
print(type(how_))               #<class 'tuple'>
print(how_[4])                  #python
print(len(how_))                #7
print(max(how_[6]))             #90
print(max(how_[4]))             #y
print(how_.index('python'))     #4
print(how_.count('python'))     #1


METHODS
-------
1. index()
2. count()
    
TASK
----

list_ = [56, [1, 2], ['python', 'java', ['python is a language', 153, 90], [78, 6], 'I know C']]
find
1. know
2. 153

print(list_[2][1])
'''

any_= [99, 44, 66, 33, 55, 22, 11, 88, 77]
print(sorted(any_))
any_.sort()

