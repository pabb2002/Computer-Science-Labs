# Pranav Abbaraju
# variables, assignment operator, reassignment

# What is a variable in programming?
# A variable is a memory location stored in RAM 
# It can hold different values
# Variables must have a unique identifier or name 

name = "Steven" # declaring age, initializing age to 38
Name = "Tim" # variables can never have the same identifier
age = 38 # the = is known as the assignment operator
		 # the left side is the memory side
		 # the right side is the data being stored to the left
gpa = 1.5		 

# reassignment
print name		 
name = "Bob"
print name

# reassignment is using an already declared variable
print age # prints 38
age = age + 10 # right side is 38 + 10
			   # left is 48
			   # more than once
print age # prints 48






# variable and a literal

# called literals, literals do not change

print 5
print 3.5 
print "hello"

print type(5)		# int
print type(3.5)		# float
print type("Hello") # string (str)







a = raw_input("Enter a side of a triangle:: ")
b = raw_input("Enter another side of a triangle:: ")
c = raw_input("Enter the hypotenuse of a triangle:: ")

a = a ** 2;
b = b ** 2;
c = c ** 2;
# a^2 + b^2 = c^2
print a + "+" + b + "=" + c