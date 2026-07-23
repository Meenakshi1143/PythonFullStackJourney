

                                                REGULAR EXPERSSIONS(RegEx)


RegEx: It is an Sequence of characters that can form searching pattern
--> To use the RegEx we have to import re module...
Syntax: import re

Functions:
1. fundall()
--> It will find all the char that are in the string.
Ex:
import re
text_ = 'Python is a Programming language and also called as dynamically typed'
print(re.findall('a', text_))

import re
text_ = 'Python is a Programming language and also called as dynamically typed'
print(re.findall('[am]', text_))     #['a', 'a', 'm', 'm', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'm', 'a']

2. search()
--> This search() will find the char, but it will give the first sequence that found in the string..
Ex:
import re
text_ = 'Python is a Programming language and also called as dynamically typed'
print(re.search('[a]', text_))        #<re.Match object; span=(10, 11), match='a'>
print(re.search('[P]', text_))        #<re.Match object; span=(0, 1), match='P'>


3. split()
Ex:
import re
text_ = 'Python is a Programming language and also called as dynamically typed'
print(re.split(' ', text_))          #['Python', 'is', 'a', 'Programming', 'language', 'and', 'also', 'called', 'as', 'dynamically', 'typed']  

4. sub()
Ex:
import re
text_ = 'Python is a Programming language and also called as dynamically typed'
print(re.sub(' ','.', text_))        #Python.is.a.Programming.language.and.also.called.as.dynamically.typed
print(re.sub(' ','*', text_))        #Python*is*a*Programming*language*and*also*called*as*dynamically*typed

5. fullmatch()

 

***Metachar
-----------
[]:-
Ex:
import re
text_ = 'Python is a Programming language and also called as dynamically typed'
print(re.findall('[Pay]', text_))       #['P', 'y', 'a', 'P', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'y', 'a', 'a', 'y', 'y']

import re
text_ = 'I have 500 Rupees'
print(re.findall('[a-z]', text_))       #['h', 'a', 'v', 'e', 'u', 'p', 'e', 'e', 's']
print(re.findall('[A-Z]', text_))       #['I', 'R']
print(re.findall('[0-9]', text_))       #['5', '0', '0']

print(re.search('[a-z]', text_))        #<re.Match object; span=(2, 3), match='h'>
print(re.search('[A-Z]', text_))        #<re.Match object; span=(0, 1), match='I'>
print(re.search('[0-9]', text_))        #<re.Match object; span=(7, 8), match='5'>

^:-
Ex:
import re
text_ = 'I have 500 Rupees'
print(re.findall('^I have', text_))     #['I have']
print(re.search('have', text_))         #<re.Match object; span=(2, 6), match='have'>

$:-
Ex:
import re
so_ = 'I am going to school'
print(re.findall('I$', so_))           #[]
print(re.search('I$', so_))            #None

print(re.findall('school$', so_))      #['school']
print(re.search('school$', so_))       #<re.Match object; span=(14, 20), match='school'>

.:-
Ex:
import re
so_ = 'Hello! This is Meenakshi'
print(re.findall('T..s', so_))         #['This']
print(re.findall('M....', so_))        #['Meena']
print(re.findall('i.', so_))           #['is', 'is']
print(re.search('i.', so_))            #<re.Match object; span=(9, 11), match='is'>


*:-
Ex:
import re
str_ = 'python module will going to complete this week'
print(re.findall('p.*n', str_))       #['python module will goin']
print(re.findall('p.*hon', str_))     #['python']
print(re.findall('p.*', str_))        #['python module will going to complete this week']

print(re.search('p.*n', str_))        #<re.Match object; span=(0, 23), match='python module will goin'>
print(re.search('p.*hon', str_))      #<re.Match object; span=(0, 6), match='python'>
print(re.search('p.*', str_))         #<re.Match object; span=(0, 46), match='python module will going to complete this week'>

+:-
Ex:
import re
str_ = 'python module will going to complete this week'
print(re.findall('p.+', str_))       #['python module will going to complete this week']
print(re.findall('p.+ython', str_))  #[]

print(re.search('p.+', str_))        #<re.Match object; span=(0, 46), match='python module will going to complete this week'>
print(re.search('p.+ython', str_))   #None

{}:-
Ex:
import re
str_ = 'Python is a language'
print(re.findall('P.{10}', str_))         #['Python is a']
print(re.findall('h.{13}', str_))         #['hon is a langu']
print(re.search('P.{10}', str_))          #<re.Match object; span=(0, 11), match='Python is a'>







