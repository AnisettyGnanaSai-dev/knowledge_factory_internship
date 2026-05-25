#comprehension is compact way to creata a collections
#in python we have list,set,dictionary,generator comprehensions
#comprehensions are more readable and efficient than traditional loops for creating collections

#list comprehension
squares = [x**2 for x in range(5)]
print(squares) # Output: [0, 1, 4, 9, 16]
#here we are creating a list of squares of numbers from 0 to 4 using list comprehension which is more concise and readable than using a traditional for loop to achieve the same result

#even or odd numbers using list comprehension
even = [x for x in range(10) if x%2 == 0]
odd = [x for x in range(10) if x%2 != 0]
print(even) # Output: [0, 2, 4, 6, 8]
print(odd) # Output: [1, 3, 5, 7, 9]

parity = ['EVEN' if x%2 == 0 else 'ODD' for x in range(10)]
print(parity) # Output: ['EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD']

# 3 X 3 matrix using list comprehension
matrix = [[[num for num in range(3)] for _ in range(3)] for _ in range(3)]
print(matrix) # Output: [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

flatten = [num for row in matrix for num in row]
print(flatten) # Output: [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]

#dictionary comprehension
squares = {x : x**2 for x in range(5)}
print(squares) # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print(word_lengths) # Output: {'apple': 5, 'banana': 6, 'cherry': 6}

#set comprehension
numbers = [1, 2, 3, 4, 5, 1, 2, 3]
squares = {x**2 for x in numbers}
print(squares) # Output: {1, 4, 9, 16, 25} here the duplicates are removed automatically because sets only store unique values

#generator comprehension
total = sum(x**2 for x in range(1000))
print(total) # Output: 332833500 this will calculate the sum of squares of numbers from 0 to 999 using a generator expression which is more memory efficient than creating a list of squares and then summing it up because generator expressions do not store the entire list in memory at once.

#difference bewtween list comprehension and generator comprehension is that list comprehension returns a list while generator comprehension returns a generator object which can be iterated over to get the values one at a time without storing the entire list in memory.
total1 = [sum(x**2 for x in range(1000))]
print(total1) # Output: [332833500] here we are creating a list with a single element which is the sum of squares of numbers from 0 to 999 using a generator expression inside the list comprehension. This is not memory efficient because we are creating a list to store the result while we can directly get the result using a generator expression without creating an intermediate list.
