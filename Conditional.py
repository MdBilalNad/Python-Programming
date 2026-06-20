#This is going to be about conditional statements.
#Conditional statements are used to perform different actions based on different conditions.
#The most common conditional statements are if, elif, and else.
#The if statement is used to test a specific condition. If the condition is true, the code block inside the if statement will be executed.
#The elif statement is used to test another condition if the previous condition was false. You can have as many elif statements as you want.
#The else statement is used to execute a block of code if all the previous conditions were false. You can only have one else statement.
#Here is an example of how to use conditional statements in Python:

age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are an adult.")
elif age > 120:
    print("You are not human.")    
else:
    print("You are a senior.")
#In this example, we are checking the value of the variable age. If age is less than 18, it will print "You are a minor." If age is equal to 18, it will print "You are an adult." If age is greater than 18, it will print "You are a senior."

