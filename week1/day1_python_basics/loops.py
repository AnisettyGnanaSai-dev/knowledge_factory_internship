#loops are used to repeat a block of code multiple times. In Python, we have two main types of loops: for loops and while loops.
#for loops are used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. The syntax is:
for i in range(5):
    print(i)
#In this example, the for loop will iterate over the range of numbers from 0 to 4 (5 is not included) and print each number.
#while loops are used to repeat a block of code as long as a certain condition is true. The syntax is:
count = 0
while count < 5:
    print(count)
    count += 1
for i in range(1, 11,3):
    print(i)
#In this example, the for loop will iterate over the range of numbers from 1 to 10 (11 is not included) with a step of 3, so it will print 1, 4, and 7.
#string iteration
name = "Coastal Seven"
for char in name:
    print(char)
#loop else statement
for i in range(5):
    print(i)
else:
    print("Loop completed")

name = "Sai"
for letter in name[::-1]: # this will iterate through the string in reverse order
    if letter == "a":
        continue
    print(letter)

for i in range(3):
    print(i)
    i = 100
for i in "123":
    print(i * 2)