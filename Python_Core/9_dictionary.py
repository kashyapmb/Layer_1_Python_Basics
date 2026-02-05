# dictionary
# Creating a dictionary
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing values in a dictionary
print(my_dict['name'])  # Output: Alice
print(my_dict.get('age'))  # Output: 30

# Adding a new key-value pair to the dictionary
my_dict['country'] = 'USA'
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}

# Updating an existing key-value pair
my_dict['age'] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}

# Removing a key-value pair from the dictionary
del my_dict['city']
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}

# Iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 31

# Checking for the presence of a key in the dictionary
print('name' in my_dict)  # Output: True
print('city' in my_dict)  # Output: False

# Length of a dictionary
print(len(my_dict))  # Output: 3

# Nested dictionaries
nested_dict = {
    'person1': {'name': 'Alice', 'age': 30},
    'person2': {'name': 'Bob', 'age': 25}
}
print(nested_dict)  # Output: {'person1': {'name': 'Alice', 'age': 30}, 'person2': {'name': 'Bob', 'age': 25}}
print(nested_dict['person1']['name'])  # Output: Alice

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

 
# keys, values, and items
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'country'])
print(my_dict.values())  # Output: dict_values(['Alice', 31, 'USA'])
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('country', 'USA')])




students = {"person1": {"name": "Alice", "age": 30, "subjects": {"Math": 85, "Science": 90}}, "person2": {"name": "Bob", "age": 25, "subjects": {"Math": 75, "Science": 80}}}
print(students["person1"]["subjects"]["Math"])  # Output: 85


# get method with default value
print(my_dict.get('name'))  # Output: Alice
print(my_dict.get('city'))  # Output: None
print(my_dict.get('city', 'Not Found'))  # Output: Not Found




