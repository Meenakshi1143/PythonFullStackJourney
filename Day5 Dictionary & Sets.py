'''

                              DICTIONARY
                              ----------

--> Dictionary is a key value pair separated by :, and  keys are unique
--> in the place of keys we have  to use immutable datatype.....

--> dict is a mutable ()

    ex:
    details_ = {"Name" : "Meenakshi", "number" : 1 , (6, 7) : [1,2]}
    print(details_)


    bank_details = {
    "Name" : "Meenakshi",
    "Mobile" : 1234567890,
    "Aadhaar No." : "123456789012",
    }
    print(bank_details)

METHODS
-------
1. keys() - used to get all the keys from the dictionary
    syntax - var_Name.keys()
    ex:
    print(bank_details.keys())        #dict_keys(['Name', 'Mobile', 'Aadhaar No.'])
    
2. values() - used to get all the values from the dictionary
    syntax - var_Name.values()
    ex:
    print(bank_details.values())      #dict_values(['Meenakshi', 1234567890, '123456789012'])

3. items() - used to get both key and value in a pair
    syntax - var_Name.items()
    ex:
    print(bank_details.items())       #dict_items([('Name', 'Meenakshi'), ('Mobile', 1234567890), ('Aadhaar No.', '123456789012')])

4. clear() - used to remove all data present in dictionary
    syntax - var_name.clear()
    ex:
    bank_details.clear()
    print(bank_details)               #{}

5. update()

    ex:
    bank_details.update({"Name" : "Meena"})
    print(bank_details)               #{'name': 'Meena', 'Mobile': 1234567890, 'Aadhaar No.': '123456789012'}



                             SETS
                             ----
--> Set is a collection of unordered elements  that are sepearted by ,
--> Set is muttable
--> can remove duplicate value by itself...
    ex:
    set_ = {1, 2, 3, 4, 2}
    print(set_)

METHODS()
--------

1. union() (|) - used to combine the elements from both sets
    syntax - set_1.union(set_2)
    ex:
    set1_ = {1, 2, 3, 4}
    set2_ = {4, 5, 6, 7}
    print(set1_ | set2_)                 #{1, 2, 3, 4, 5, 6, 7}
    print(set1_.union(set2_))            #{1, 2, 3, 4, 5, 6, 7}

2. intersection() (&) - common elements from both sets
    syntax - set_1.intersection(set_2)
    ex:
    print(set1_ & set2_)                     #{4}
    print(set1_.intersection(set2_))         #{4}

3. Symmetric Difference() ^ - all different elements from both sets
    syntax - set_1.symmetric_difference(set_2)
    ex:
    print(set1_ ^ set2_)                         #{1, 2, 3, 5, 6, 7}
    print(set1_.symmetric_difference(set2_))     #{1, 2, 3, 5, 6, 7}

4. add() - used to add new elements into set
    syntax - var_name.add()
    ex:
    set1_ = {1, 2, 3, 4}
    set1_.add(5)
    print(set1_)

5. remove() - used to delete elements from set
    syntax - var_name.remove()
    ex:
    set1_.remove(1)
    print(set1_)              #{2, 3, 4}

6. pop() -
    syntax - var_name.pop()
    ex:
    set1_.pop()               #{2, 3, 4}
    print(set1_)

    
    set1_ = {10, 1, 2, 3, 4}

    set1_.pop()
    print(set1_)             #{2, 3, 4, 10}

7. discard() -
    syntax - var_name.discard()
    ex:
    set1_.discard(9)
    print(set1_)               #{1, 2, 3, 4}
    set1_.discard(4)
    print(set1_)               #{1, 2, 3}

    
'''



set1_ = {10, 1, 2, 3, 4}

set1_.pop()
print(set1_)









