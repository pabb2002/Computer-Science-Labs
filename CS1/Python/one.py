# Pranav Abbaraju
'''
# multiples of 3 and 5 
y = 0
for x in range(1, 1000):
	if x%3 == 0 or x%5 == 0:
		y += x
print y
'''
# even fibonacci numbers
yOne = 1
print yOne
yTwo = 2
print yTwo
newY = yOne + yTwo

sum = 0
if yOne%2 == 0:
	if yTwo%2 == 0:
		if newY%2 == 0:
			sum += yOne + yTwo + newY
		elif newY%2 == 1:
			sum += yOne + yTwo
	elif yTwo%2 = 1:
		if newY%2 == 0:
			sum += yOne + newY
		elif newY%2 == 1:
			sum += yOne
elif yOne%2 == 1:
	if yTwo%2 == 0:
		if newY%2 == 0:
			sum += yTwo + newY
		elif newY%2 == 1:
			sum += yTwo
	elif yTwo%2 = 1:
		if newY%2 == 0:
			sum += newY
		elif newY%2 == 1:
			sum += yOne
	
			sum += yOne + newY
elif yTwo%2 == 0:
elif newY%2 == 0
print newY
for x in range(3999997):
	yOne = yTwo
	yTwo = newY
	newY = yOne + yTwo
	sum += newY
	print newY
print sum


