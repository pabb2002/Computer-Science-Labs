# Pranav Abbaraju
# Loops Lab 2

print "mini lab #10 - diagonalNStars:"
def diagonalNStars(num):
	star = ""
	numCount = num
	for x in range(num):
		numCount -= 1  
		for y in range(x):
			star += " "
		star += "*"
		for y in range(numCount):
			star += " "
		star += "\n"		
	return star 
print diagonalNStars(int(raw_input("Enter the number of stars to be printed: ")))
print diagonalNStars(int(raw_input("Enter the number of stars to be printed: ")))
print diagonalNStars(int(raw_input("Enter the number of stars to be printed: ")))

#_______________________________________________________________________________________


print "mini lab #11 - reverseDiagonalNStars:"
def reverseDiagonalNStars(num):
	star = ""
	numCount = num
	for x in range(num):
		numCount -= 1  
		for y in range(numCount):
			star += " "
		star += "*"
		for y in range(x):
			star += " "
		star += "\n"		
	return star
print reverseDiagonalNStars(int(raw_input("Enter the number of stars to be printed: ")))
print reverseDiagonalNStars(int(raw_input("Enter the number of stars to be printed: ")))
print reverseDiagonalNStars(int(raw_input("Enter the number of stars to be printed: ")))

#_______________________________________________________________________________________


print "mini lab #11 - VStars:"
def VStars(num):
	star = ""
	numCount = num
	for x in range(num):
		numCount -= 2
		star += "*"  
		for y in range(numCount):
			star += " "
		star += "*"
		star += "\n"		
	return star

