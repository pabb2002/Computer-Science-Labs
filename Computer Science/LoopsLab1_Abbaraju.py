# Pranav Abbaraju
# Loops Lab 1

print "mini Lab #1 - row5Stars"
def rowFiveStars():
	x = 0 
	star = ""
	while x < 5:
		star += "*"
		x += 1
	return star
print rowFiveStars()
print ""

# ____________________________________________________


print "mini Lab #2 - row5Stars2" 
def rowFiveStarsTwo():
	star = ""
	for x in range(5):
		star += "*"
	return star
print rowFiveStarsTwo()
print ""

#______________________________________________________


print "mini Lab #3 - rowNStars"
def rowNStars(num):
	x = 0
	star = ""
	while x < num:
		star += "*"
		x += 1
	return star  
print rowNStars(int(raw_input("Enter the number of stars to be printed: ")))
print rowNStars(int(raw_input("Enter the number of stars to be printed: ")))
print rowNStars(int(raw_input("Enter the number of stars to be printed: ")))
print ""

#______________________________________________________


print "mini Lab #4 - rowNStars2"
def rowNStarsTwo(num):
	star = ""
	for x in range(num):
		star += "*"
	return star
print rowNStarsTwo(int(raw_input("Enter the number of stars to be printed: ")))
print rowNStarsTwo(int(raw_input("Enter the number of stars to be printed: ")))
print rowNStarsTwo(int(raw_input("Enter the number of stars to be printed: ")))
print ""

#______________________________________________________


print "mini Lab #5 - colNStars" 
def colNStars(num):
	x = 0
	star = ""
	while x < num:
		star += "*\n"
		x += 1
	return star
print colNStars(int(raw_input("Enter the number of stars to be printed: ")))
print colNStars(int(raw_input("Enter the number of stars to be printed: ")))
print colNStars(int(raw_input("Enter the number of stars to be printed: ")))
print ""
	
#______________________________________________________


print "mini Lab #6 - colNValues" 
def colNValues(num):
	x = 0
	y = ""
	while x < num:
		x += 1
		y += str(x) + "\n" 
	return y
print colNValues(int(raw_input("Enter the number of values to be printed: ")))
print colNValues(int(raw_input("Enter the number of values to be printed: ")))
print ""
	
#______________________________________________________


print "mini Lab #7 - MtoNValues" 
def MtoNValues(numOne, numTwo):
	y = str(numOne)
	num = numOne
	for x in range(numOne, numTwo):
		num += 1
		y += " " + str(num)
	return y
print MtoNValues(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))
print MtoNValues(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))
print MtoNValues(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))
print ""

#______________________________________________________


print "mini Lab #8 - MtoNEvens" 
def MtoNEvens(numOne, numTwo):
	if numOne%2 == 0:
		y = str(numOne) + " "
	elif numOne%2 == 1:
		y = ""
	x = numOne
	while x < numTwo:
		if numOne%2 == 1:
			numOne += 1
			y += str(numOne) + " " 
		elif numOne%2 == 0: 
			numOne +=1
		x += 1		
	return y 
print MtoNEvens(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))
print MtoNEvens(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))
print MtoNEvens(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))
print ""

#______________________________________________________


print "mini Lab #9 - MtoNOdds" 
def MtoNOdds(numOne, numTwo):
	if numOne%2 == 1:
		y = str(numOne) + " "
	elif numOne%2 == 0:
		y = ""
	x = numOne
	while x < numTwo:
		if numOne%2 == 0:
			numOne += 1
			y += str(numOne) + " " 
		elif numOne%2 == 1: 
			numOne +=1
		x += 1
	return y  
print MtoNOdds(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))
print MtoNOdds(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))
print MtoNOdds(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))
print ""