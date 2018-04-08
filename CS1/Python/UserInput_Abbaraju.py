# Pranav Abbaraju
# User input, methods

# What is a method? What does it look like?
# What do they do?

# A method is an action the program can do
# type() is a method: unique identifier followed by ()

# user input: to get user input you need to use the 
# following method: raw_input(). To store the values
# entered by the user, you need a variable

userName = raw_input("Enter your user name: ") # prompt
print userName
print type(userName)

age = int(raw_input("Enter your age: "))
print age
print type(age)

gpa = float(raw_input("Enter your GPA: "))
print gpa
print type(gpa) 

# concatenation: the joining of strings using + sign
print userName + ", " + str(age) + ", " + str(gpa) 