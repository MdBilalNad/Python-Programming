# This is about sets in Python
# A set is an unordered collection of unique elements

# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements from a set
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Checking if an element is in a set
print(4 in my_set)  # Output: True
print(3 in my_set)  # Output: False

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3}

# Difference
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}

# Symmetric Difference
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Set comprehension
squared_set = {x**2 for x in range(1, 6)}
print(squared_set)  # Output: {1, 4, 9, 16, 25}

e = set() # Creating an empty set
print(e)  # Output: set()