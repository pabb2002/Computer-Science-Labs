#import math

from math import *
#* is wildcard, if you don't use it you have to type 
#library name
# Pranav Abbaraju
# Method Stuff

print type(5) #5 is an int, value, parameter

#print math.sqrt(64)

print sqrt(64)
print hypot(3, 4)

#types of methods
#1. simple methods
def hypotenuse(side1, side2): #method header
	#a^2 + b^2 = c^2
	c = ((side1**2) + (side2**2)) ** .5
	print c
hypotenuse(4, 6) # does not account for value, just prints
#2. return methods
def hypotenuse(side1, side2): #method header
	#a^2 + b^2 = c^2
	c = ((side1**2) + (side2**2)) ** .5
	return c
print hypotenuse(4, 6) # acts as value - float