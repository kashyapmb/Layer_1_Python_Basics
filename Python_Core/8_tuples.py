# Tuples in Python are ordered, immutable collections of items. They are similar to lists but cannot be modified after creation.
# Creating a tuple
my_tuple = (1, 2, 3, 'Hello', 4.5)
print(my_tuple)  # Output: (1, 2, 3, 'Hello', 4.5)

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1 (first element)
print(my_tuple[3])  # Output: 'Hello' (fourth element)

# Tuples are immutable, so we cannot modify elements
# my_tuple[1] = 'World'  # This will raise a TypeError
# However, we can create a new tuple by concatenating existing tuples
new_tuple = my_tuple + (6, 7)
print(new_tuple)  # Output: (1, 2, 3, 'Hello', 4.5, 6, 7)

# Tuple slicing
print(my_tuple[1:4])  # Output: (2, 3, 'Hello') (slices from index 1 to 3)

# Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c')

# Tuple repetition
repeated_tuple = tuple1 * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)

# Checking for membership in a tuple
print(2 in tuple1)  # Output: True
print('d' in tuple2)  # Output: False

# Length of a tuple
print(len(my_tuple))  # Output: 5

# Iterating through a tuple
for item in my_tuple:
    print(item)

# Tuple unpacking
a, b, c, d, e = my_tuple
print(a)  # Output: 1
print(d)  # Output: Hello

# Nested tuples (tuples within tuples)
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)  # Output: ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0])  # Output: (1, 2) (first sub-tuple)
print(nested_tuple[0][1])  # Output: 2 (second element of the first sub-tuple)

# Converting a list to a tuple
list_to_tuple = [1, 2, 3, 4]
converted_tuple = tuple(list_to_tuple)
print(converted_tuple)  # Output: (1, 2, 3, 4)

# Converting a tuple to a list
tuple_to_list = (5, 6, 7, 8)
converted_list = list(tuple_to_list)
print(converted_list)  # Output: [5, 6, 7, 8]

# Counting occurrences of an element in a tuple
count_tuple = (1, 2, 2, 3, 4, 2)
print(count_tuple.count(2))  # Output: 3

# Finding the index of the first occurrence of an element in a tuple
print(count_tuple.index(3))  # Output: 3

# Single element tuple (note the comma)
single_element_tuple = (42,)
print(single_element_tuple)  # Output: (42,)

# Empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()

# Swapping values using tuples
x = 10
y = 20
x, y = y, x
print(x)  # Output: 20
print(y)  # Output: 10

# Using tuples as dictionary keys
my_dict = {('a', 1): 'value1', ('b', 2): 'value2'}
print(my_dict[('a', 1)])  # Output: value1

# Copy() method does not exist for tuples since they are immutable, but we can create a new tuple that is a copy of an existing one
original_tuple = (1, 2, 3)
copied_tuple = tuple(original_tuple)
print(copied_tuple)  # Output: (1, 2, 3)

