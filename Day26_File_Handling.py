
                                File Handling

--> File handler is an object that gives more options like creating , updating.

Two ways to open the file:
1. open()
Syntax:
do = open('file_name', 'mode')

close()

Ex:
do = open('ABCDED.txt', 'r')
print(do.read())
do.close()

2. with(keyword)
Syntax:
with open('file_name', 'mode') as do:
Ex:
with open('ABCDEF.txt', 'r') as do:
    print(do.read())

Modes:
r - Used to read the file, incase if the file is not present it will raise error.
w - Used to write the text inside the file and it will override the text inside the file. Incase if the file is not present it will create a new file with the name given
Ex:
with open('ABCDEFGHIJK.txt', 'w') as do:
    print(do.write("Hii Good Morning...\nToday we are going to discuss about File handling in python."))

a - This is used to add the text at last position inside the file.
Ex:
with open('ABCDEFGHIJK.txt', 'a') as do:
    print(do.write("\nFile handler is an object that gives more options like creating , updating."))


x - Used to create a new file by adding the text inside the file. Incase if the file is present it will raise an error...
Ex:
with open('AAAA.txt', 'x') as do:
    print(do.write("Codegnan Visakhapatnam"))


***write() - This function is used to add the text inside a file or update a file with new text..
Ex:
with open('AAAA.txt', 'w') as do:
    print(do.write("We are from batch - 004"))  # write()-- w mode is used to earse previous text and update with new text

with open('AAAA.txt', 'a') as do:
    print(do.write("We are from batch - 004")) # append a mode is used to add the given text in end
    
***read() - Used to read file and this read() will read file chunk by chunk....
         We can also specify the size
Ex:
with open('ABCDEF.txt', 'r') as do:
    print(do.read(10))  # Using read(10) gives the output with 10 character of text which is present in the file

***readline() - This readline() will read only one line at a time.
Ex:
with open('ABCDEFGHIJK.txt', 'r') as do:
    print(do.readline())
    
***readlines() - This function will read whole file and give it in a list each line is one index in that list...
Ex:
with open('AAAA.txt', 'r') as do:
    print(do.readlines())



with open('AAAA.txt', 'r') as do:
    print(do.readlines())     #['Codegnan, Visakhapatnam \n', 'We are from batch - 004\n', 'Python full stack\n']
    print(do.readline())      #


with open('AAAA.txt', 'r') as do:
    print(do.readline())      #Codegnan, Visakhapatnam 
    print(do.readlines())     #['We are from batch - 004\n', 'Python full stack\n']





Example:
with open('file11.txt', 'r') as so:
    print(so.read())              #Hii Good Morning


with open('file11.txt', 'w') as so:
    print(so.write("\nThis is Meenakshi"))

with open('file11.txt', 'a') as so:
    print(so.write("\nCurrent Python FullStack trainee at Codegnan, Visakhaptam"))

with open('file11.txt', 'r') as so:
    print(so.readline())          #This is Meenakshi

with open('file11.txt', 'r') as so:
    print(so.readlines())         #['This is Meenakshi\n', 'Current Python FullStack trainee at Codegnan, Visakhaptam']
    
with open('file11.txt', 'r+') as so:
    print(so.read())
    print(so.write("\nToday I'm going to learn new topic File Handling"))

with open('file11.txt', 'w+') as so:
    print(so.write("\nFile Handling: File handler is an object that gives more options like creating , updating."))
    so.seek(0)
    print(so.read())




    

