'''

                                        GENERATORS
                                        ----------

--> This generator is a special function that returns the itertor. instead of returning all the values at once.
--> Here we are going to use yeild keyword
--> This is called lazy evolution
Ex:
def some_():
    yield 1
    yield 2
    yield 3
so_= some_()
print(next(so_))
print(next(so_))
print(next(so_))


Working of Generator
--------------------
--> When a function is called
--> It does not execute the function immediately
--> It will returns the generator object
--> Then the function will pause at each yield
--> When the next() is called again, execution resumes from where it stopped.
Ex:
def demo_():
    print("start")
    yield 1
    print('Middle')
    yield 2
    print('End')
    yield 3
how_ = demo_()
print(next(how_))


WITH GENERATOR
Ex:
def how_(so_):
    for i in range(so_):
        yield i * i
any_ = how_(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))


WITHOUT GENERATOR
EX:
def sqt(n):
    for i in range(n):
        print(i * i)
sqt(5)



yield keyword
-------------

--> This will produces the value
--> But the yield pauses the function
--> And yield will save functions current state
--> Yield will continue where it stoped

next() Keyword
--------------
--> The next() function is used to retrieve the next value from a generator
Ex:
def how_(so_):
    for i in range(so_):
        yield i * i
any_ = how_(5)
print(next(any_))
print(next(any_))

StopIteration
-------------
--> Calling next() function after all values retrieve then it will raise StopIteration exception
Ex:
def how_(so_):
    for i in range(so_):
        yield i * i
any_ = how_(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))# Extra calling next() function gives output as StopIteration



EXAMPLES:
---------
1.
def add_(a, b):
    yield a + b
any_ = add_(4, 6)
print(next(any_))


2.
count_ = 0
def fun_(n, count_):
    for i in range(1, n):
        yield i ** i
        count_ += 1
        
any1_ = fun_(5, count_)
print(next(any1_))
print(next(any1_))
print(next(any1_))


GENERATOR EXPRESSION
--------------------
--> The Generator experssion is similar to a list comprehension but uses paranthesis()instead of []
Ex:
gen_ = (x * x for x in range(1, 6))
print(next(gen_))
print(next(gen_))
print(next(gen_))
print(next(gen_))
print(next(gen_))


'''

gen_ = (x * x for x in range(1, 6))
print(next(gen_))
print(next(gen_))
print(next(gen_))
print(next(gen_))
print(next(gen_))
