# Lists in Python are ordered, mutable collections of items. They can contain elements of different data types and are defined using square brackets [].
# Creating a list
my_list = [1, 2, 3, 'Hello', 4.5]
print(my_list)  # Output: [1, 2, 3, 'Hello', 4.5]

# Accessing elements in a list
print(my_list[0])  # Output: 1 (first element)
print(my_list[3])  # Output: 'Hello' (fourth element)

# Modifying elements in a list
my_list[1] = 'World'
print(my_list)  # Output: [1, 'World', 3, 'Hello', 4.5]

# Adding elements to a list
my_list.append(6)  # Adds 6 to the end of the list
print(my_list)  # Output: [1, 'World', 3, 'Hello', 4.5, 6]


# Removing elements from a list
my_list.remove('Hello')  # Removes 'Hello' from the list
print(my_list)  # Output: [1, 'World', 3, 4.5, 6]

# List slicing
print(my_list[1:4])  # Output: ['World', 3, 4.5] (slices from index 1 to 3)

# List concatenation
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 'a', 'b', 'c']

# List repetition
repeated_list = list1 * 2
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3]

# Checking for membership in a list
print(2 in list1)  # Output: True
print('d' in list2)  # Output: False

# Length of a list
print(len(my_list))  # Output: 5
# Iterating through a list
for item in my_list:
    print(item)

# List comprehension to create a new list based on an existing list
squared_list = [x**2 for x in list1]
print(squared_list)  # Output: [1, 4, 9]

# Nested lists (lists within lists)
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list)  # Output: [[1, 2], [3, 4], [5, 6]]
print(nested_list[0])  # Output: [1, 2] (first sublist)
print(nested_list[0][1])  # Output: 2 (second element of the first sublist)

# sorting a list
unsorted_list = [3, 1, 4, 1, 5]
unsorted_list.sort()  # Sorts the list in place
print(unsorted_list)  # Output: [1, 1, 3, 4, 5]

# Sorting a list in reverse order
unsorted_list.sort(reverse=True)  # Sorts the list in reverse order
print(unsorted_list)  # Output: [5, 4, 3, 1, 1]

# Reversing a list
unsorted_list1 = [3, 1, 4, 1, 5]
unsorted_list1.reverse()  # Reverses the list in place
print(unsorted_list1)  # Output: [5, 1, 4, 1, 3]

# insert an element at a specific index
my_list.insert(2, 'Inserted')  # Inserts 'Inserted' at index 2
print(my_list)  # Output: [1, 'World', 'Inserted', 3, 4.5, 6]

# Popping an element from the list
popped_element = my_list.pop()  # Removes and returns the last element
print(popped_element)  # Output: 6
print(my_list)  # Output: [1, 'World', 'Inserted', 3, 4.5]


