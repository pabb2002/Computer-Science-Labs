print "mini lab #10 - diagonalNStars:"
def diagonalNStars(num):
	star = ""
	for x in range(num):
		for y in range(x):
			star += " "
		star += "*"
		star += "\n"		
	return star 
print diagonalNStars(int(raw_input("Enter the number of stars to be printed: ")))
print diagonalNStars(int(raw_input("Enter the number of stars to be printed: ")))
print diagonalNStars(int(raw_input("Enter the number of stars to be printed: ")))
print ""
print ""

#________________________________________________________________________________________


print "mini lab #11 - reverseDiagonalNStars:"
def reverseDiagonalNStars(num):
	star = ""
	for x in range(num, 0, -1):
		for y in range(x):
			star += " "
		star += "*"
		star += "\n"		
	return star 
print reverseDiagonalNStars(int(raw_input("Enter the number of stars to be printed: ")))
print reverseDiagonalNStars(int(raw_input("Enter the number of stars to be printed: ")))
print reverseDiagonalNStars(int(raw_input("Enter the number of stars to be printed: ")))
print ""
print ""

#________________________________________________________________________________________


print "mini lab #12 - VStars:"
def VStars(num):
	star = ""
	numCount = num*2 
	for x in range(num):
		numCount -= 2
		for y in range(x):
		  star += " "
		star += "*"  
		for y in range(numCount):
			star += " "
		star += "*"
		star += "\n"	
	return star
print VStars(int(raw_input("Enter the number of stars to be printed: ")))
print VStars(int(raw_input("Enter the number of stars to be printed: ")))
print VStars(int(raw_input("Enter the number of stars to be printed: ")))
print ""
print ""

#________________________________________________________________________________________


print "mini lab #13 - DiamondNStars:"
def diamondNStars(num):
  star = ""
  numCount = -3
  for x in range(num-1, -1, -1):
    numCount += 2
    for y in range(x):
      star += " "
    star += "*"
    if numCount != -1:
      for y in range(numCount):
        star += " "
    if x != num-1:
      star += "*"
    star += "\n"
  for x in range(1, num):
    numCount -= 2
    for y in range(x):
      star += " "
    star += "*"
    for y in range(numCount):
      star += " "
    if x != num-1:
      star += "*"
    star += "\n"
  return star
print diamondNStars(int(raw_input("Enter the number of stars to be printed: ")))
print diamondNStars(int(raw_input("Enter the number of stars to be printed: ")))
print diamondNStars(int(raw_input("Enter the number of stars to be printed: ")))





