#list is a collection of items in a particular order.it is a mutable data type in python which means we can change the items in a listafter it  has been created.
#list is ordered,mutable,allows duplicate items"""
"""Important list methods
append() - adds an item to the end of the list
extend() - adds all items of a list to another list
insert() - adds an item at a specified position 
remove() - removes the first item with the specified value
pop() - removes the item at the specified position  
clear() - removes all items from the list
index() - returns the index of the first item with the specified value
count() - returns the number of items with the specified value
sort() - sorts the items in the list
reverse() - reverses the order of the items in the list
copy() - returns a copy of the list
"""
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(names) # Output: ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
#accessing list items
print(names[0]) # Output: Alice

names.append("Anji")
print(names) # Output: ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Anji']
names.insert(1, "gnani")
print(names) # Output: ['Alice', 'gnani', 'Bob', 'Charlie', 'David', 'Eve', 'Anji']
names.remove("Alice")
print(names) # Output: ['gnani', 'Bob', 'Charlie', 'David', 'Eve', 'Anji']
names.pop(2)
print(names) # Output: ['gnani', 'Bob', 'David', 'Eve', 'Anji']
names.clear()
print(names) # Output: []
names.extend(["Gnani", "Anji", "Surya"])
print(names) # Output: ['Gnani', 'Anji', 'Surya']
names.append("Gnani")
print(names.index("Gnani")) # Output: 0
print(names.count("Gnani")) # Output: 2
names.sort()
print(names) # Output: ['Anji', 'Gnani', 'Gnani', 'Surya']
names.reverse()
print(names) # Output: ['Surya', 'Gnani', 'Gnani', 'Anji']
names.remove("Gnani")
print(names) # Output: ['Surya', 'Gnani', 'Anji']
names_copy = names.copy()
print(names_copy) # Output: ['Surya', 'Gnani', 'Anji']

#removing duplicates from a list
numbers = [1, 2, 3, 4, 5, 1, 2, 3]
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
print(unique) # Output: [1, 2, 3, 4, 5]

"""| Function      | Purpose                     |
| ------------- | --------------------------- |
| `sum()`       | Adds all numbers            |
| `max()`       | Largest value               |
| `min()`       | Smallest value              |
| `len()`       | Number of elements          |
| `sorted()`    | Sort list                   |
| `reversed()`  | Reverse iterator            |
| `any()`       | Checks if at least one True |
| `all()`       | Checks if all True          |
| `enumerate()` | Gives index + value         |
| `zip()`       | Combines lists              |
| `map()`       | Applies function            |
| `filter()`    | Filters values              |
"""
num = [1, 2, 3, 4, 5]
print(sum(num)) # Output: 15
print(max(num)) # Output: 5 
print(min(num)) # Output: 1
print(len(num)) # Output: 5
print(sorted(num, reverse=True)) # Output: [5, 4, 3, 2, 1]
#difference between sorted() and sort() is that sorted() returns a new sorted list while sort() modifies the original list in place.
print(list(reversed(num))) # Output: [5, 4, 3, 2, 1]
list1 = ["", [], 0, None, False]
print(all(list1)) # Output: False
list1.append("Hello")
print(any(list1)) # Output: True
print(all(list1)) # Output: False

print(enumerate(num)) # Output: <enumerate object at 0x7f8c8c8c8c8>
for index, value in enumerate(num):
    print(index, value)

list2 = ["Gnani", "Anji", "Surya"]
print(zip(num, list2)) # Output: <zip object at 0x7f8c8c8c8c8>
for n, name in zip(num, list2):
    print(n, name)

print(list(map(lambda x: x**2, num))) # Output: [1, 4, 9, 16, 25]
print(list(filter(lambda x: x % 2 == 0, num))) # Output: [2, 4]