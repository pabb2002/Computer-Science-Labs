# Pranav Abbaraju
# Loops Lab 1

def rowFiveStars():
	x = 0 
	star = ""
	while x < 5:
		star += "*"
		x += 1
	return star
print rowFiveStars()

# ____________________________________________________


def rowFiveStarsTwo():
	star = ""
	for x in range(5):
		star += "*"
	return star
print rowFiveStarsTwo()

#______________________________________________________


def rowNStars(num):
	x = 0
	star = ""
	while x < num:
		star += "*"
		x += 1
	return star  
print rowNStars(int(raw_input("Enter an integer: ")))

#______________________________________________________


def rowNStarsTwo(num):
	star = ""
	for x in range (num):
		star += "*"
	return star  
print rowNStarsTwo(int(raw_input("Enter an integer: ")))

#______________________________________________________


def colNStars(num):
	x = 0
	star = ""
	while x < num:
		star += "*\n"
		x += 1
	return star
print colNStars(int(raw_input("Enter an integer: ")))
	
#______________________________________________________


def colNValues(num):
	x = 0
	y = ""
	while x < num:
		x += 1
		y = y + str(x) + "\n" 
	return y
print colNValues(int(raw_input("Enter an integer: ")))
	
#______________________________________________________


def MtoNValues(numOne, numTwo):
	y = str(numOne)
	for x in range (numOne, numTwo):
		numOne += 1
		y += " " + str(numOne)
	return y
print MtoNValues(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))
print MtoNValues(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))
print MtoNValues(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))


#______________________________________________________


def MtoNEvens(numOne, numTwo):
	if numOne%2 == 0:
		y = str(numOne) + " "
	elif numOne%2 == 1:
		y = ""
	for x in range (numOne, numTwo):
		if numOne%2 == 1:
			numOne += 1
			y += str(numOne) + " " 
		elif numOne%2 == 0: 
			numOne +=1
	return y 
print MtoNEvens(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))
print MtoNEvens(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))
print MtoNEvens(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))


#______________________________________________________


def MtoNOdds(numOne, numTwo):
	if numOne%2 == 1:
		y = str(numOne) + " "
	elif numOne%2 == 0:
		y = ""
	for x in range (numOne, numTwo):
		if numOne%2 == 0:
			numOne += 1
			y += str(numOne) + " " 
		elif numOne%2 == 1: 
			numOne +=1
	return y  
print MtoNOdds(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))
print MtoNOdds(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))
print MtoNOdds(int(raw_input("Enter the starting value to be printed: ")), int(raw_input("Enter the stopping value: ")))