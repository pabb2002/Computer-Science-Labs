# Pranav Abbaraju
# Methods and Libraries

# What is a method?      a grouping of code statements 
# Why do we use methods? allows for the reuse of code 
# What is a library?     a collection of classes and methods
# Why do we use libraries? use classes and methods that have
# already been made

# def key word meaning: define
# pickRandom is the method name
# method name is followed by ()

# importing allows the use of other classes
import random # import statement

def pickRandom(): # method header: simple method
# all statements need to be tabbed in order to be placed
# in the method
	print random.randint(25,50)  # parameters - variables
								 # passed from one part of
								 # code into the method

 
#anything inside the parentheses is a parameter
def squareRoot(num): # method header: return method
	return num **.5
		
# when using a method with a parameter, the value is passed at 
# the method's method call		
print squareRoot(16) # method call		
# to display output of return method, a print is needed

#How do I use a method?
print pickRandom() #method call
# simple methods do not need a print in front to display output

import math

print math.sqrt(squareRoot(625))

# suing the pythagorean theorem that you created before
# ask the user for two sides of a triangle
# and return the value of the hypotenuse in a method call


#HOW MANY METHOD TYPES ARE THERE? There are two types of methods:
#simple method and return (returns a value) method 
#WHAT ARE THE 5 THINGS NEEDED TO MAKE + USE A METHOD? 
#The five things needed are:
#def
#name
#parentheses
#parameter (variable that is specific to the method)
#a colon (:)
#an indent on the next line, then 
#a method call - name()
								