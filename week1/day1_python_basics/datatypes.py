#main basic datatypes in python
#string
#int
#float
#boolean
#complex

string_var = "Hello, Coastal seven!"
int_var = 25
float_var = 3.14
boolean_var = True
complex_var = 2 + 3j

#twisted example
x = 0.1 #because of the way floating point numbers are represented in binary, 0.1 cannot be represented exactly, leading to precision issues when performing arithmetic operations with it.
y = 0.2
print(x + y) # this will not give 0.3 due to floating point precision issues    
x = True
y = True
print(x + y) # this will give 2 because in Python, True is treated as 1 and False is treated as 0 when used in arithmetic operations.

print(type(string_var)) # <class 'str'>
print(type(int_var)) # <class 'int'>
z = input("Enter a value: ")
print(z * 3) # this will repeat the input value 3 times if it's a string, or perform multiplication if it's a number.
#the * operator is overloaded in Python, meaning it can perform different operations based on the types of the operands. When used with strings, it repeats the string a specified number of times. When used with numbers, it performs multiplication.