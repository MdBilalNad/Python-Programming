#this is going to be about lists in python

#creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)

#Multiple data types in a list
my_list2 = [1, "Hello", 3.14, True]
print(my_list2)

#List slicing
print(my_list[0]) #first element
print(my_list[1]) #second element
print(my_list[-1]) #last element
print(my_list[0:3]) #first three elements
print(my_list[2:]) #from third element to end
print(my_list[:3]) #first three elements
print(my_list[::2]) #every second element
print(my_list[::-1]) #reverse the list

#lists are mutable
my_list[0] = 10
print(my_list)

#list functions
print(len(my_list)) #length of the list

my_list.append(6) #add an element to the end of the list
print(my_list)

my_list.insert(0, 0) #add an element at a specific position
print(my_list)

my_list.remove(3) #remove the first occurrence of an element
print(my_list)

my_list.pop() #remove and return the last element
print(my_list)

my_list.pop(0) #remove and return the first element
print(my_list)

my_list.clear() #remove all elements from the list
print(my_list)

my_list.sort() #sort the list
print(my_list)

my_list2.reverse() #reverse the list
print(my_list2)

my_list2.count(1) #count the number of occurrences of 1
print(my_list2)

#Sum of elements in a list
print(sum(my_list)) #sum of elements in the list

