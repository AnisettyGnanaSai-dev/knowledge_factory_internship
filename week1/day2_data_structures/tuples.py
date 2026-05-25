#tuples is same as list but it is immutable
#tuples are defined using parentheses ()
#tuples are faster ,safer and more memory efficient than lists
#we can unpack tuples into variables and we used in API's and functions,machine learning and data science
#we can use tuples as keys in dictionaries
#we can use tuples to return multiple values from a function
#we can use tuples to store heterogeneous data

person = ("Alice", 30, "Engineer")
name,age,profession = person
print(name) # Output: Alice
print(age) # Output: 30
print(profession) # Output: Engineer

def calculate(a, b):
    sum = a + b
    product = a * b
    return sum, product
result = calculate(5, 10)
print(result) # Output: (15, 50)
#here the result came as a tuple and we can unpack it into variables

#in tuple unlike list we dont have many methods we have only count() and index() methods
numbers = (1, 2, 3, 4, 5, 1, 2, 3)
print(numbers.count(1)) # Output: 2
print(numbers.index(3)) # Output: 2

a = 0
b = 1
a, b = b, a
print(a) # Output: 1
print(b) # Output: 0
#this is called tuple unpacking and it is a common technique used to swap values without using a temporary variable

#in tuple we have inbuilt functions like sum(), max(), min(), len(), sorted() etc
num = (1, 2, 3, 4, 5)
print(sum(num)) # Output: 15
print(max(num)) # Output: 5 
print(min(num)) # Output: 1
print(len(num)) # Output: 5
print(sorted(num, reverse=True)) # Output: [5, 4, 3, 2, 1]
#here the sorted() function returns a list because tuples are immutable and we cannot sort them in place like lists

data = 1, 2, 3
print(data) # Output: (1, 2, 3)
#internally python treats this as a tuple even without parentheses and it is called tuple packing

locations = {
    (17.385044, 78.486671): "Hyderabad",
    (28.613939, 77.209023): "Delhi",
    (19.076090, 72.877426): "Mumbai"
}
#here the keys are tuples beacause they are immutable and can be used as keys in dictionaries while lists cannot be used as keys because they are mutable.
print(locations[(17.385044, 78.486671)]) # Output: Hyderabad

n, *m = 1, 2, 3, 4, 5
print(n) # Output: 1
print(m) # Output: [2, 3, 4, 5],Advanced unpacking with * operator allows us to unpack a tuple into a variable and the rest of the values into a list.

import sys
n = (1, 2, 3, 4, 5)
m = [1, 2, 3, 4, 5]
print(sys.getsizeof(n)) # Output: 48
print(sys.getsizeof(m)) # Output: 96
#here we can see that the tuple takes less memory than the list because tuples are immutable and
#they are optimized for memory usage while lists are more flexible and can grow and shrink in size.

data1 = ([1, 2, 3], [4, 5, 6])
data1[0][0] = 10
print(data1) # Output: ([10, 2, 3], [4, 5, 6])
#here we can see that even though the tuple is immutable we can still modify the mutable objects inside the tuple like lists. This is because the immutability of a tuple only applies to the tuple itself, not to the objects it contains.

#Tuple itself is immutable, but it may contain mutable objects whose internal state can change.