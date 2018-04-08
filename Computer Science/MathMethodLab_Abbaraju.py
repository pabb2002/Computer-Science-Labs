# Pranav Abbaraju
# Math Method Lab

from math import *

def distance(num1, num2):
	dis = abs(num1 - num2)
	return "The distance from " + str(num1) + " to " + str(num2) + " is " + str(dis)
print distance(3, 5)
print distance(-3.3, 5.8)
print distance(65, -88)
print distance(24.9, 1678.4)

print ""

def areaVolumeLength(num):
	squareArea = int(pow(num, 2))
	sphereVolume = round((4 * pi * pow(num, 3))/3, 1)
	squareSideLength = round(sqrt(num), 2)
	print "The area of a square whose side length is " +str(num) + " is " + str(squareArea)
	print "The volume of a sphere whose radius is " + str(num) + " is " + str(sphereVolume)
	print "The side length of a square whose area is " + str(num) + " is " + str(squareSideLength)
areaVolumeLength(5)
areaVolumeLength(82)

print ""

def sheetsPlywood(roofArea):
	numOfSheets = int(ceil(float(roofArea)/float(32)))
	return "A " + str(roofArea) + " square-foot roof needs a minimum of " + str(numOfSheets) + " sheets of plywood"
print sheetsPlywood(200)
print sheetsPlywood(988)

print ""

def maxDVDs(num):
	numOfDVDs = int(floor(num/8.99))
	return "With " + "$" + str(num) + ", " + "Johnny can buy " + str(numOfDVDs) + " DVDs"
print maxDVDs(26.25)
print maxDVDs(53.94)