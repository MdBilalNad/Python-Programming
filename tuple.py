# This is going to be about tuples in python

# creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Multiple data types in a tuple
my_tuple2 = (1, "Hello", 3.14, True)
print(my_tuple2)

# Tuple slicing
print(my_tuple[0]) # first element
print(my_tuple[1]) # second element
print(my_tuple[-1]) # last element
print(my_tuple[0:3]) # first three elements
print(my_tuple[2:]) # from third element to end
print(my_tuple[:3]) # first three elements
print(my_tuple[::2]) # every second element
print(my_tuple[::-1]) # reverse the tuple

# tuples are immutable
# my_tuple[0] = 10 # this will raise an error

# tuple functions
print(len(my_tuple)) # length of the tuple
print(my_tuple.count(1)) # count the number of occurrences of 1
print(my_tuple.index(3)) # find the index of the first occurrence of 3
print(my_tuple2.index("Hello")) # find the index of the first occurrence of "Hello"

#Concatenation of tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)

#Membership testing
print(1 in my_tuple) # True
print(10 in my_tuple) # False

#minimum and maximum of a tuple
print(min(my_tuple)) # 1
print(max(my_tuple)) # 5
