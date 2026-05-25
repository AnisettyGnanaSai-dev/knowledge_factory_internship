#dictionaries in python are also known as hash maps or associative arrays in other programming languages. They are used to store key-value pairs and provide fast access to values based on their keys.
#dictionaries are mutable, which means we can change their contents after they are created. We can add, remove, or modify key-value pairs in a dictionary.
#dictionaries are defined using curly braces {} and key-value pairs are separated by colons :. Each key-value pair is separated by a comma ,. Keys in a dictionary must be unique and immutable, which means they can be of any data type that is hashable, such as strings, numbers, tuples, etc. Values in a dictionary can be of any data type and can be duplicated.
#dictionaries are unordered, which means that the order of key-value pairs is not guaranteed. However, starting from Python 3.7, dictionaries maintain the insertion order of key-value pairs.

student = {
    "name": "Gnani",
    "age": 20,
    "grade": "A"
}

print(student["name"])
student["cgpa"] = 9.5#adding a new key-value pair to the dictionary
print(student) # Output: {'name': 'Gnani', 'age': 20, 'grade': 'A', 'cgpa': 9.5}
student["age"] = 21 #modifying the value of an existing key
print(student) # Output: {'name': 'Gnani', 'age': 21, 'grade': 'A', 'cgpa': 9.5}
del student["grade"] #removing a key-value pair from the dictionary
print(student) # Output: {'name': 'Gnani', 'age': 21, 'cgpa': 9.5}

dict = {}#empty dictionary
print(dict) # Output: {}

#in dictionaries we have different methods like get(), keys(), values(), items(), pop(), popitem(), clear(), update(),copy() etc
student1 = {
    "name": "Anji",
    "age": 22,
    "grade": "B"
}
print(student1.get("name")) # Output: Anji
print(student1.keys()) # Output: dict_keys(['name', 'age', 'grade'])
print(student1.values()) # Output: dict_values(['Anji', 22, 'B'])
print(student1.items()) # Output: dict_items([('name', 'Anji'), ('age', 22), ('grade', 'B')])

for key, value in student1.items():
    print(f"{key}: {value}")

print(student1.pop("grade")) # Output: B this will remove the key-value pair with the key "grade" and return its value
print(student1.popitem()) # Output: ('age', 22) this will remove and return an arbitrary key-value pair from the dictionary
student1.update({"cgpa": 8.75, "roll_no": 127 }) # this will add a new key-value pair to the dictionary
#if already exists it will update the value of the existing key(overwrite the existing value)
print(student1) # Output: {'name': 'Anji', 'cgpa': 8.75, 'roll_no': 127}
student1_copy = student1.copy() # this will create a shallow copy of the dictionary
print(student1_copy) # Output: {'name': 'Anji', 'cgpa': 8.75, 'roll_no': 127}

print(student1.clear()) # this will remove all key-value pairs from the dictionary

students = {
    "student1": {"name": "Gnani", "age": 20, "grade": "A+"},
    "student2": {"name": "Anji", "age": 22, "grade": "B"},
    "student3": {"name": "Surya", "age": 21, "grade": "A"}
}

students.setdefault("student4", {"name": "Lakshmi", "age": 23, "grade": "A+"}) # this will add a new key-value pair to the dictionary if the key "student4" does not already exist
print(students) # Output: {'student1': {'name': 'Gnani', 'age': 20, 'grade': 'A+'}, 'student2': {'name': 'Anji', 'age': 22, 'grade': 'B'}, 'student3': {'name': 'Surya', 'age': 21, 'grade': 'A'}, 'student4': {'name': 'Lakshmi', 'age': 23, 'grade': 'A+'}}

#dictionaries built-in functions
print(len(students)) # Output: 4 this will return the number of key-value pairs in the dictionary
print(max(students, key=lambda k: students[k]["grade"])) # Output: student1 this will return the key with the maximum value based on the grade of the students
print(min(students, key=lambda k: students[k]["age"])) # Output: student1 this will return the key with the minimum value based on the age of the students

students.setdefault(students["student1"]["age"], 21) # this will add a new key-value pair to the dictionary with the key as the age of student1 and the value as 21 if the key does not already exist
print(students) # Output: {'student1': {'name': 'Gnani', 'age': 20, 'grade': 'A+'}, 'student2': {'name': 'Anji', 'age': 22, 'grade': 'B'}, 'student3': {'name': 'Surya', 'age': 21, 'grade': 'A'}, 'student4': {'name': 'Lakshmi', 'age': 23, 'grade': 'A+'}, 20: 21}

#frequency counter
s = "gnani anji surya gnani anji"
k = s.split()
f = {}
for c in k:
    f[c] = f.get(c, 0) + 1
print(f) # Output: {'gnani': 2, 'anji': 2, 'surya': 1} this will count the frequency of each word in the string and store it in a dictionary where the key is the word and the value is its frequency
