str = "abcdefghi"

# Slicing from index 0 to 6 (not including 6)
print(str[0:6])  # Output: abcdef   

# Slicing from the beginning to index 7 (not including 6)
print(str[:7])   # Output: abcdefg

# Slicing from index 7 to the end of the string
print(str[7:])   # Output: hi

# Slicing the entire string
print(str[:])    # Output: abcdefghi

# Slicing with a step of 2
print(str[::2])  # Output: acegi

# Slicing with a step of 3 from index 1 to index 8 (not including 8)
print(str[1:8:3])  # Output: beh

# Slicing with negative indices from -5 to -1 (not including -1)
print(str[-5:-1])  # Output: efgh

# Slicing with a negative step to reverse the string
print(str[::-1]) # Output: ihgfedcba

# Slicing with a negative step from index 8 to index 2 (not including 2)
print(str[8:2:-1])  # Output: ihgfed

# Slicing with a negative step from index 10 to the beginning
print(str[2::-1])  # Output: cba



                                                                          