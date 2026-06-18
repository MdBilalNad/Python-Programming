#these are the methods of dictionary in python

marks = {
    "Bilal": 90,
    "Hoor": 89,
    "Ali": 80,
    "Sara": 79
}

marks.items() #returns a list containing a tuple for each key value pair
print(marks.items())

marks.keys() #returns a list containing the dictionary's keys
print(marks.keys())

marks.values() #returns a list containing the dictionary's values
print(marks.values())   

marks.get("Bilal") #returns the value of the specified key
print(marks.get("Bilal"))

marks.update({"Hoor": 90}) #updates the value of the specified key
print(marks)

print(marks.get("Bilal"))
print(marks["Bilal"]) 
#both of these will give the same output but the get method will not give an error if the key is not found, it will return None instead. The [] method will give an error if the key is not found.

marks.pop("Ali") #removes the specified key and returns the corresponding value
print(marks)
