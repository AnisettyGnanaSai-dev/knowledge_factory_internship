#json means javascript object notation it is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.
# It is based on a subset of the JavaScript programming language and is commonly used for transmitting data in web applications.

import json 

#converting a python object to a json string
data = {
    "name": "Gnani",
    "age": 30
}
json_string = json.dumps(data, indent=4) # this will convert the python object to a json string with an indentation of 4 spaces for better readability
print(type(json_string)) # Output: <class 'str'>
print(json_string)  # Output: {"name": "Gnani", "age": 30}

#converting a json string to a python object
json_string = '{"name": "Gnani", "age": 30}'
data = json.loads(json_string)
print(type(data)) # Output: <class 'dict'>
print(data) # Output: {'name': 'Gnani', 'age': 30}

json_string1 = '''{
    "student": {
    "name": "Gnani",
    "age": 30},
    "courses": ["Python", "Java", "C++"],
    "is_graduated": false
}'''
data1 = json.loads(json_string1)
print(type(data1)) # Output: <class 'dict'>
print(data1) # Output: {'name': 'Gnani', 'age': 30}

with open("states.json", "r") as file:
    data = json.load(file) # this will read the json data from the file and convert it to a python object
print(type(data)) # Output: <class 'dict'>
print(data) # Output: {'country': 'India', 'states': [{'state': 'Andhra Pradesh', 'capital': 'Amaravati'}, {'state': 'Arunachal Pradesh', 'capital': 'Itanagar'}, ...]}

with open("states.json", "w") as file:
    json.dump(data, file, indent = 5) # this will write the python object to the file in json format with an indentation of 5 spaces for better readability