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
#result = divide(5, 0) # when you run this code, it will pause at the line with pdb.set_trace(), and you can use commands like 'n' to step to the next line, 'p' to print the value of variables, and 'c' to continue execution until the next breakpoint or the end of the program. This can help you understand the flow of the program and identify where the error is occurring, which in this case is when b is zero.

#3. using assertions: you can use assertions to check if certain conditions are met in your code. For example:
def amount(a):
    #assert a > 0, "a must be greater than 0" # this will raise an AssertionError if a is not greater than 0
    return a + 10
result = amount(-5) # this will raise an AssertionError because a is not greater than 0. The assertion will help you identify that the value of a is not valid and is causing the error.

#whether the developers assumptions are correct or not, and if not, it will raise an error with a message that can help you understand what went wrong.

"""Assertions can be disabled in optimized Python runs.
So:
useful for debugging/development
not ideal for critical runtime validation"""

#4. using logging: you can use the logging module in Python to log messages at different levels. For example:
#logging means recording messages that can help you understand the flow of the program and identify where the error is occurring. 
# You can use the logging module in Python to log messages at different levels (e.g., debug, info, warning, error, critical) and configure the logging output to a file or console.
#Logs are the “memory” of software systems. They are used to record events, errors, and other information that can help developers understand the behavior of the system and identify issues.
"""Because logging provides:

timestamps
log levels
file saving
filtering
scalability
production monitoring"""

"""Main Log levels:
DEBUG: Detailed information, typically of interest only when diagnosing problems.
INFO: Confirmation that things are working as expected.
WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., ‘disk space low’). The software is still working as expected.
ERROR: Due to a more serious problem, the software has not been able to perform some function.
CRITICAL: A serious error, indicating that the program itself may be unable to continue running."""

import logging
#logging.debug("This is a debug message") # this will log a debug message
#this will not be logged because the default logging level is WARNING, which means that only messages with a level of WARNING or higher will be logged. You can change the logging level to DEBUG to see this message.

logging.basicConfig(filename="app.log", level=logging.DEBUG,format ='%(asctime)s - %(levelname)s - %(message)s') # this will configure the logging to show messages with a level of DEBUG or higher, and include the timestamp, log level, and message in the log output.
f = 10
g = 0
try :
    result = f / g # this will raise a ZeroDivisionError because you cannot divide by zero.
except ZeroDivisionError as e:
    logging.error("An error occurred: %s", e) # this will log an error message with the details of the exception. The logging output will include the timestamp, log level, and message, which can help you understand what went wrong and identify where the error is occurring.

