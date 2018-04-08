#Pranav Abbaraju
# Guess the Number
# Computer generates a random number and the user has to try and guess it


	
# casting
# What is casting? changing between types
	
"5" #how would I cast an str to become an int?
int ("5")
# what happens when I cast a float to an int??
3.74
int(3.74) # will return 3 
# age # error does not know what is going on!! runtime error	
	
	
# errors
# three main errors
# 1. syntax errors - because you misspell something, forgot punctuation
# typed a reserved word as your own, for every ( you need a )
# 2. runtime errors - when you have an error in execution 
# example - print "help" + 5
# 3. logic errors - when you don't know what you are doing!!

# user input
# do you always have to save user input into a variable?? NNOO
bMonth = int(raw_input("Enter your birth month: "))
bMonth = bMonth + int(raw_input("Enter your birth day: "))#user input 
#can be used just as a value, not always being saved in a variable
print bMonth

#escape sequences
print "\"" #puts a quotation mark in str
print "\\" #puts \ in str
print "\t" #puts a new tab or 5 spaces in str
print "\n" #puts a new line in str

#variables
# What is a naming convention called for naming variables? - camelCase
# toMakeSomeStuff - 1st letter of 1st word is lowercase, every other 1st
# letter of each additional word is Uppercase
# Can you have spaces in variable names? - NO
# Can you have underscores in variable names? - YES
# Can you have symbols in variable names - NO
# Can you have a number start the name of a variable? - NO
# What is a variable? storage location in memory, the name given can be used
# in your code

#math operators
# +            Addition
# -            Subtraction
# /            Float division
# //           Int division
# %            Remainder division
# *            Multiplication
# **           Exponent
# also (), but it is technically not an operator
# order of first
