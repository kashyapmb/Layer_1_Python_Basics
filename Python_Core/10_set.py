# Set information
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
# Creating a set
my_set = {1, 2, 3, 'Hello', 4.5}
print(my_set)  # Output: {1, 2, 3, 'Hello', 4.5}

# Accessing elements in a set
# Sets are unordered, so we cannot access elements by index
# However, we can check for the presence of an element in a set
print(2 in my_set)  # Output: True
print('World' in my_set)  # Output: False

# Adding an element to a set
my_set.add('New Element')
print(my_set)  # Output: {1, 2, 3, 'Hello', 4.5, 'New Element'}

# Removing an element from a set
my_set.remove(2)
print(my_set)  # Output: {1, 3, 'Hello', 4.5, 'New Element'}

# Iterating through a set
for item in my_set:
    print(item)

# Length of a set
print(len(my_set))  # Output: 5

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Union of sets
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection of sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Difference of sets
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Set comprehension
squared_set = {x**2 for x in range(5)}
print(squared_set)  # Output: {0, 1, 4, 9, 16}

# Frozen sets (immutable sets)
frozen_set = frozenset([1, 2, 3, 'Hello', 4.5])
print(frozen_set)  # Output: frozenset({1, 2, 3, 'Hello', 4.5})

# Converting a list to a set
list_to_set = [1, 2, 3, 4, 4, 5]
converted_set = set(list_to_set)
print(converted_set)  # Output: {1, 2, 3, 4, 5} (duplicates are removed)

# Converting a set to a list
set_to_list = {1, 2, 3, 'Hello', 4.5}
converted_list = list(set_to_list)
print(converted_list)  # Output: [1, 2, 3, 'Hello', 4.5] (order may vary)


# Empty Set
set1 = {1, 2, 3}
print(set1)
set1.clear()
print(set1)


# Remove a random value
set2 = {1, 3, 6, 10}
num = set2.pop()
print(set2)
print(num)