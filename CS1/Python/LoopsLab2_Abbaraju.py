# Pranav Abbaraju
# Loops Lab 2

print "mini lab #10 - diagonalNStars:"
def diagonalNStars(num):
	stars = ""
	space = ""
	for x in range(num):
		for y in range(1):
			space += " "
			stars += "*\n" + space 
	return stars
print diagonalNStars(int(raw_input("Enter the number of stars to be printed: ")))
print diagonalNStars(int(raw_input("Enter the number of stars to be printed: ")))
print diagonalNStars(int(raw_input("Enter the number of stars to be printed: ")))
print ""

#__________________________________________________________________________________


print "mini lab #11 - reverseDiagonalNStars"
def reverseDiagonalNStars(num):
	stars = ""
	space = " "*num
	while x in range(num):
		space -= " "
		 