#Pranav Abbaraju

# Relational Operators
#1.	greater than or equal to: >=
#2.	not equal: !=	
#3.	less than: <
#4.	greater than: >
#5.	less than or equal to: <=
#6.	equals: ==

# Logic Operators
#1. and
# logic table for "and"
# T and F = F
# F and T = F
# F and F = F
# T and T = T
#2. or
# logic table for "or"
# T or F = T
# F or T = T
# F or F = F
# T or T = T
#3. not: don't worry about this one

# print ("true" == "True") #condition, it has a relational operator
# print "False" == "False" # True or False: True
# print "true" == "True" and "False" == "False" 
# print "true" == "True" or "False" == "False" 
# print "True" == "True" and "False" == "False" 

# if statement - for true output
# to write an if statement, the following is needed:
# if (condition) :
#if 3 < 4:
#	print "Less than"
#print "Greater than" # this is not part of the if statement
# if else statement
#if 52 < 4:
#	print "Less than"
#else: # else is for the false output
#	print "Greater than"
# if elif statement
#grade = 80
#if grade > 70 and grade < 90:
#	print "Passing"
#elif grade >= 90:
#	print "'A' Grade"
#else:
#	print "FAILING"


def belt(score):
	if score < 2:
		print "You are a red belt" 
	elif score < 3:
		print "You are a blue belt"
	elif score < 4:
		print "You are an orange belt"
	else:
		print "You are a black belt"
belt(int(raw_input("Enter your score:: ")))