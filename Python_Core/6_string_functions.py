str= "KashyapBavadiya"

# Convert the string to uppercase
print(str.upper())  # Output: KASHYAPBAVADIYA

# Convert the string to lowercase
print(str.lower())  # Output: kashyapbavadiya

# Capitalize the first letter of the string
print(str.capitalize())  # Output: Kashyapbavadiya

# Count the occurrences of a substring
print(str.count('a'))  # Output: 4

# Find the index of the first occurrence of a substring
print(str.find('B'))  # Output: 7

# Replace a substring with another substring
print(str.replace('Bavadiya', 'Patel'))  # Output: KashyapPatel

# Split the string into a list of substrings based on a delimiter
"""Internally, Python needs something to split on (space, comma, letter, etc.).
An empty string "" is ambiguous — Python doesn’t know where to split."""
print(str.split('a'))  # Output: ['K', 'shy', 'pB', 'v', 'diy', ''] 

# Check if the string starts with a specific substring
print(str.startswith('Kash'))  # Output: True

# Check if the string ends with a specific substring
print(str.endswith('Bavadiya'))  # Output: True

# Strip whitespace from the beginning and end of the string
str_with_spaces = "   Hello, World!   "
print(str_with_spaces.strip())  # Output: "Hello, World!"

# Join a list of strings into a single string with a specified delimiter
str_list = ['Kashyap', 'Bavadiya']  
print(' '.join(str_list))  # Output: "Kashyap Bavadiya"

# Get the length of the string
print(len(str))  # Output: 15

# Check if the string is numeric
numeric_str = "12345"
print(numeric_str.isnumeric())  # Output: True

# Check if the string is alphabetic
alpha_str = "Kashyap"
print(alpha_str.isalpha())  # Output: True

# Check if the string is alphanumeric
alnum_str = "Kashyap123"
print(alnum_str.isalnum())  # Output: True

# Format the string using f-strings
name = "Kashyap"
age = 21
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Kashyap and I am 21 years old.

# Center the string within a specified width, padding with spaces
print(str.center(20))  # Output: "   KashyapBavadiya   "

# Check if the string is all uppercase
print(str.isupper())  # Output: False

# Check if the string is all lowercase
print(str.islower())  # Output: False

# Swap the case of each character in the string
print(str.swapcase())  # Output: kASHYAPbAVADIYA

# Title case the string (first letter of each word capitalized)
print(str.title())  # Output: Kashyapbavadiya

# Expand tabs in the string to spaces
tabbed_str = "Kashyap\tBavadiya"
print(tabbed_str.expandtabs(4))  # Output: Kashyap    Bavadiya

# Check if the string is printable
print(str.isprintable())  # Output: True
