#Pranav Abbaraju
#Evens

def printEvens(bob):
	output = ""
	for x in range(len(bob)):
		if bob[x]%2 == 0:
			output += str(bob[x]) + "\n"
	return output

bob = [3,5,6,33,1,10,12,17,20,5]
print printEvens(bob)
bob = [32,52,62,33,12,10,12,17,20,52]
print printEvens(bob) 