#functions are reusable blocks of code that perform a specific task. They allow you to break down complex problems into smaller, manageable pieces.
#In Python, you can define a function using the def keyword, followed by the function name and parentheses. The code block within the function is indented.
def greet(name):
    print("Hello, " + name + "!")
greet("Coastal Seven")

#functions consists of a function name, parameters (optional), and a function body. The parameters are placeholders for the values that will be passed to the function when it is called. The function body contains the code that will be executed when the function is called.
#parameters and arguments: parameters are the variables that are defined in the function definition, while arguments are the actual values that are passed to the function when it is called. For example:
def add(a, b):
    return a + b
result = add(5, 3)
print(result)

#default parameters: you can assign default values to parameters in a function definition. This allows you to call the function without providing arguments for those parameters, and the default values will be used. For example:
def greet(name="Coastal Seven"):
    print("Hello, " + name + "!")
greet() # this will use the default value "Coastal Seven"
greet("Gnana Sai") # this will override the default value with "Gnana Sai"

#multiple returns : a function can return multiple values by separating them with commas. When you call the function, it will return a tuple containing all the returned values. For example:
def get_name_and_age():
    name = "Gnana Sai"
    age = 21
    return name, age
name, age = get_name_and_age()
print("Name:", name)
print("Age:", age)

#args and kwargs: *args and **kwargs are used to pass a variable number of arguments to a function. *args allows you to pass a variable number of non-keyword arguments, while **kwargs allows you to pass a variable number of keyword arguments. For example:
def print_args(*args):
    for arg in args:
        print(arg)
print_args(1, 2, 3, "Hello", [4, 5, 6])
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + str(value))
print_kwargs(name="Gnana Sai", age=21, college="Anits")

#lambda functions: lambda functions are anonymous functions that can have any number of arguments but only one expression. They are often used for short, simple functions that are not reused elsewhere in the code. For example:
num_list = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, num_list))) # this will double each element in the num_list

def greet(name):
    print("Hello, " + name + "!")
x = greet("Coastal Seven")
print(x) # this will print None because the greet function does not return any value, it only prints a message. In Python, if a function does not have a return statement, it returns None by default.

#nested functions: a function defined inside another function is called a nested function. Nested functions can access variables from the enclosing function's scope. For example:
def outer():

    def inner():
        print("Inner")

    inner()

outer()

#lambda function
students = [
    ("Gnani", 85),
    ("Rahul", 90),
    ("Sai", 75)
]

students.sort(key=lambda x: x[1]) # this will sort the students list based on the second element of each tuple (the score)
print(students)