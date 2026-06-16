a = 'Bilal' #single quote
# b = "Bilal" #double quote
# c = '''Bilal''' #triple quote
# d = """Bilal""" #triple quote
print(a)
# print(b)
# print(c)
# print(d)
 
 
#String Slicing
print(a[0]) #first character
print(a[1]) #second character
print(a[-1]) #last character
print(a[0:3]) #first three characters
print(a[2:]) #from third character to end
print(a[:3]) #first three characters
print(a[::2]) #every second character
print(a[::-1]) #reverse the string
print(a[1:5:2]) #from second to fifth character, every second character

#String length 

length = len(a)
print("the length of the string is: ",length)

print(a.endswith('l')) #check if the string ends with 'l'
print(a.startswith('B')) #check if the string starts with 'B'
print(a.upper()) #convert to uppercase
print(a.lower()) #convert to lowercase
print(a.replace('B','M')) #replace 'B' with 'M'
print(a.split('i')) #split the string at 'i'

#string Functions
print(a.isalpha()) #check if all characters are alphabetic
print(a.isdigit()) #check if all characters are digits
print(a.isalnum()) #check if all characters are alphanumeric
print(a.isspace()) #check if all characters are whitespace
print(a.count('l')) #count the number of occurrences of 'l'
print(a.find('l')) #find the index of the first occurrence of 'l'
print(a.index('l')) #find the index of the first occurrence of 'l' (raises an error if not found)
print(a.rfind('l')) #find the index of the last occurrence of 'l'
print(a.rindex('l')) #find the index of the last occurrence of 'l' (raises an error if not found)
