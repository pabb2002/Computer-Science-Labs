#Pranav Abbaraju
#Count

def find_smallest(bob, num):
	count = 0
	for x in range(len(bob)):
		if bob[x] == num:
			count += 1
	return count
			
bob = [3,5,6,33,111,7,7,15,-5,9,1,6,6,7,8,9,5,6,6,6,7,2,7,99,11,8]
print find_smallest(bob,6)
print find_smallest(bob,7)
print find_smallest(bob,5)