'''
                          STATEMNETS
                          ----------

1. Condition Statments
----------------------
**if --> used to check a condition is true or not
Ex:
num_ = 10
if num_ % 2 == 0:
    print(f"{num_} is even number")

**if-else --> else is the fall back statement incase that if condition is false, them this will be executed...
Ex:
num_ = int(input("Enter number: "))
if num_ % 2 == 0:
    print(f"{num_} is even number") #print(num_, "is even number")
    
else:
    print(f"{num_} is odd number")


bank_details = {"ATM PIN" : '9421'}
pin_ = input("Enter your 4 digit ATM pin: ")
if pin_ in bank_details["ATM PIN"]:
    print("Welcome to ATM !!!")
else:
    print("You have entered incorrect pin....")


**nested if --> using if inside the another if
Ex:
bank_details = {"ATM PIN" : '9421'}
pin_ = input("Enter your 4 digit ATM pin: ")
if len(pin_) == 4:
    if pin_ in bank_details["ATM PIN"]:
        print("Welcome to ATM !!!")
    else:
        print("You have entered incorrect pin....") 
else:
    print("Please enter only 4 digit pin...")



**elif
Ex:
marks_ = int(input("Enter your marks: "))
if marks_ >= 90:
    print("A+")
elif marks_ >= 80:
    print("A")
elif marks_ >= 70:
    print("B+")
elif marks_ >= 60:
    print("B")
else:
    print("Fail...")


2. Control Statments
3. Loop Statements




list_  = list(map(int,input().split()))
if len(list_) == 3:
    print(max(list_))

    

num1_ = int(input("Enter num1: "))
num2_ = int(input("Enter num2: "))
num3_ = int(input("Enter num3: "))
if num1_ > num2_ and num1_ > num3_:
    print(f"{num1_} is maximum number")
elif num2_ > num1_ and num2_ > num3_:
    print(f"{num2_} is maximum number")
else:
    print(f"{num3_} is maximum number")
    


str_ = input("Enter character: ")
list_ = ('a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
if str_ in list_:
    print(str_, "is a vowel")
else:
    print(str_,"is not vowel")

'''

list_ = list(map(int,input().split()))
if len(list_) == 3:
    if 
else:
    print("len is not matched...")

