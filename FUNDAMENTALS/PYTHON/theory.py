#PYTHON is high level programming language developed by guido van rossum in 1991 
#python is interpreted language and easy to learn.


# tokens are the smallest indivisual units.

# keywords are reserved words that have some specific meaning.  33 KEYWORDS

# literals are fixed values assinged to variables.

 # identifiers are name of the object or variables.
 # rule: not keyword ,not starts from number ,underscores are used in it .


'''operators are special symbols used in programming .
 arthematic: +,-,*,/
 relational:==,<,>,<=,>=
 logical:and ,or ,not
 bitwise:&,^,~
 asssingment:=,+=,//+
 identity: is , is not
 membership: in , not in'''



 # punctuators are also symbols (),{},[] .



 # DATA TYPES 
'''
 INTEGERS (int)           IMMUTABLE
 FLOATING (float)             "
 BOOLEAN (bool)               "            True/False
 STRING (str)                 "             WE CAN USE "",'',
 LIST                      MUTABLE
 TUPLE                    IMMUTABLE 
 DICTIANARIES              MUTABLE
 
 
 '''

# PYTHON ALLOW DYNAMIC TYPING IT MEANS WE CAN CHANGE THE TYPE OF DATA 
# MUTABLE IS CHANGABLE 
# IMMUTABLE IS NOT CHANGABLE 

#INDENTATION IS THE SPACE USED IN PYTHON WHICH MEANS THAT ARE THE PART OF PROGRAME
# USED FOR COMMENTS 
'''
✅ Functions in Python – Explained Simply
In Python, functions are reusable blocks of code that perform a specific task. They help make your code more organized, modular, and readable.

🔹 Types of Functions in Python
Built-in functions: Predefined by Python.
Examples: print(), len(), range(), input(), type()

User-defined functions: Created by the programmer.

🔹 How to Define a Function
python
Copy
Edit
def function_name(parameters):
    # code block
    return result
🔹 Example: Simple Function Without Parameters
python
Copy
Edit
def greet():
    print("Hello, welcome to Python!")
    
greet()   # Function call
🔹 Example: Function With Parameters
python
Copy
Edit
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum is:", result)
🔹 Default Parameters
python
Copy
Edit
def greet(name="Guest"):
    print("Hello", name)

greet()          # Output: Hello Guest
greet("Amit")    # Output: Hello Amit
🔹 Keyword Arguments
python
Copy
Edit
def info(name, age):
    print("Name:", name)
    print("Age:", age)

info(age=25, name="Riya")
🔹 Variable-length Arguments
*args → for variable number of positional arguments

**kwargs → for variable number of keyword arguments

python
Copy
Edit
def total(*args):
    return sum(args)

print(total(10, 20, 30))  # Output: 60

def profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

profile(name="Rahul", age=21)
🔹 Return Statement
Used to send result back from the function.

You can return any object: number, string, list, dict, etc.

python
Copy
Edit
def square(n):
    return n * n

print(square(4))   # Output: 16
🔹 Lambda Functions (Anonymous functions)
python
Copy
Edit
square = lambda x: x * x
print(square(5))   # Output: 25
✅ Summary
Concept	Syntax Example
Defining function	def func():
Calling function	func()
With parameters	def func(x, y):
Return value	return x + y
Default parameter	def func(x=0):
Variable args	def func(*args):
Keyword args	def func(**kwargs):
Lambda function	lambda x: x * x


'''