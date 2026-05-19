#debugging means finding and understanding the errors in your code and fixing them.
#There are different types of errors in Python, such as syntax errors, runtime errors, and logical errors. 
#Syntax errors occur when the code is not written correctly according to the rules of the Python language. 
# Runtime errors occur when the code is syntactically correct but encounters an error during execution.
#  Logical errors occur when the code runs without any errors but produces incorrect results.
#types of debugging techniques:
#1. print statements: you can use print statements to check the values of variables and the flow of the program at different points in the code. This can help you identify where the error is occurring and what values are causing the error.
#2. using a debugger: a debugger is a tool that allows you to step through your code line by line, inspect variables, and set breakpoints to pause the execution at specific points. This can help you understand the flow of the program and identify where the error is occurring.
#3. using assertions: assertions are statements that check if a condition is true. If the condition is false, an AssertionError is raised. You can use assertions to check if certain conditions are met in your code and identify where the error is occurring.
#4. using logging: logging is a way to record messages that can help you understand the flow of the program and identify where the error is occurring. You can use the logging module in Python to log messages at different levels (e.g., debug, info, warning, error, critical) and configure the logging output to a file or console.

#5. using unit tests: unit tests are automated tests that check if individual units of code (e.g., functions, methods) are working correctly. You can use the unittest module in Python to create and run unit tests for your code, which can help you identify where the error is occurring and ensure that your code is working as expected.

#1. print statements
def add(a, b):
    print("a:", a)
    print("b:", b)
    return a - b # this should be a + b instead of a - b
result = add(5, 3)
print(result) # this will print 2 instead of 8 because of the logical error in the add function. The print statements will help you identify that the values of a and b are correct, but the operation being performed is incorrect.

"""def divide(a, b):
    print("a:", a)
    print("b:", b)
    return a / b
result = divide(5, 0) # this will raise a ZeroDivisionError because you cannot divide by zero. The print statements will help you identify that the value of b is zero, which is causing the error."""

#2. using a debugger: you can use the built-in pdb module in Python to set breakpoints and step through your code. For example:
import pdb
def add(a, b):
    pdb.set_trace() # this will set a breakpoint at this line
    return a + b
result = add(5, 3)
print(result) # when you run this code, it will pause at the line with pdb.set_trace(), and you can use commands like 'n' to step to the next line, 'p' to print the value of variables, and 'c' to continue execution until the next breakpoint or the end of the program. This can help you understand the flow of the program and identify where the error is occurring.

def divide(a, b):
    pdb.set_trace() # this will set a breakpoint at this line
    
    return a / b
result = divide(5, 0) # when you run this code, it will pause at the line with pdb.set_trace(), and you can use commands like 'n' to step to the next line, 'p' to print the value of variables, and 'c' to continue execution until the next breakpoint or the end of the program. This can help you understand the flow of the program and identify where the error is occurring, which in this case is when b is zero.
