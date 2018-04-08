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
yTwo = 2
newY = yOne + yTwo
sum = 2

for x in range(3999997):
	yOne = yTwo
	yTwo = newY
	newY = yOne + yTwo
	if yOne%2==0:
	sum+=yOne
	if yTwo%2==0:
	sum+=yTwo
if newY%2==0:
	sum+=newY
	print newY
print sum


