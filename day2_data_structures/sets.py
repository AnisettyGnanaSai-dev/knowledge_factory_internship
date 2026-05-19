#set is an unordered collection of unique items. It is mutable, meaning you can add or remove items from it after it has been created. Sets are defined using curly braces {} or the
# built-in set() function. Sets are useful for storing unique items and performing mathematical operations like union, intersection, difference, and symmetric difference.
#sets are unordered and do not support indexing or slicing like lists and tuples. However, we can iterate over a set using a for loop or convert it to a list or tuple if we need to access its elements by index.
#duplcates can remove automatically in sets and it is a common use case for sets to remove duplicates from a list or other iterable.
#sets are also useful for membership testing, as they provide a fast way to check if an item is in a set or not. Sets are implemented as hash tables, which means that they have an average time complexity of O(1) for membership testing and adding or removing items.
#creating a set

num = {1, 2, 3, 4, 5, 2, 3}
print(num) # Output: {1, 2, 3, 4, 5}
#here the duplicates 2 and 3 are removed automatically and we get a set of unique

#empty set 
empty_set = set()
print(empty_set) # Output: set()
#not empty_set = {} this will create an empty dictionary not a set

#set methods
"""add() - adds an item to the set
update() - adds all items of a set to another set
remove() - removes the specified item from the set
discard() - removes the specified item from the set if it is present
pop() - removes and returns an arbitrary item from the set
clear() - removes all items from the set"""

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5}
print(set1 | set2) # Output: {1, 2, 3, 4, 5} the union operator | can also be used to get the union of two sets
print(set1 & set2) # Output: {3} the intersection operator & can be used to get the intersection of two sets
print(set1 - set2) # Output: {1, 2} the difference operator - can be used to get the difference of two sets
print(set1 ^ set2) # Output: {1, 2, 4, 5} the symmetric difference operator ^ can be used to get the symmetric difference of two sets
print(set1.intersection(set2)) # Output: {3}
print(set1.difference(set2)) # Output: {1, 2}
print(set1.symmetric_difference(set2)) # Output: {1, 2, 4, 5}

set3 = {1, 2, 3}
set3.add(4)
print(set3) # Output: {1, 2, 3, 4}
set3.update({5, 6})
print(set3) # Output: {1, 2, 3, 4, 5, 6}

string = {"A", "B", "C "}
string.update("DEF")
print(string) # Output: {'A', 'B', 'C ', 'D', 'E', 'F'}
#because string is iterable we can update a set with a string and it will add each character as a separate item in the set
set3.remove(6)
print(set3) # Output: {1, 2, 3, 4, 5}
set3.discard(7) # this will not raise an error because 7 is not in the set
print(set3) # Output: {1, 2, 3, 4, 5}
set3.pop() # this will remove and return an arbitrary item from the set
print(set3) # Output: {2, 3, 4, 5} the output may vary because sets are unordered and pop() removes an arbitrary item from the set
set3.clear() # this will remove all items from the set
print(set3) # Output: set()

set4 ={1, 2}
print(set1.issubset(set4)) # Output: False because set1 is not a subset of set4
print(set1.issuperset(set4)) # Output: True because set1 is a superset of set4
print(set1.isdisjoint(set3)) # Output: True because set1 and set3 have no common items

#tuples in sets are allowed but not lists because tuples are immutable and can be hashed while lists are mutable and cannot be hashed
set5 = {(1, 2), (3, 4), (5, 6)}
print(set5) # Output: {(1, 2), (3, 4), (5, 6)}

x = frozenset([1,2,3])

data = {x}

print(data) # Output: {frozenset({1, 2, 3})}
#frozenset is an immutable version of a set and it can be used as an element