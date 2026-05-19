#conditions are used to make decisions in code. They allow us to execute certain blocks of code based on whether a condition is true or false.
#In Python, we use if, elif, and else statements to create conditions.
age = 20
has_id = True

if age >= 18:

    if has_id:
        print("Entry allowed")

    else:
        print("ID required")

else:
    print("Underage")

#twisted conditions
if True and False:
    print("A")
else:
    print("B")
#twisted conditions can lead to unexpected results if not used carefully. In this example, the condition is always false because True and False cannot both be true at the same time, so it will always print "B".
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":

    if password == "python123":
        print("Login successful")

    else:
        print("Wrong password")

else:
    print("Username not found")
#In this example, the conditions check if the username is "admin" and if the password is "python123". If both conditions are true, it prints "Login successful". If the username is correct but the password is wrong, it prints "Wrong password". If the username is not found, it prints "Username not found".
"""
False0
""
[]
{}
None
"""