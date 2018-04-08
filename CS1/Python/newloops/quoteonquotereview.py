#Pranav Abbaraju
#Quiz Review 1/22/18

#Loops (for,while)
#Loops go in directions (forwards, backwards)
#Nested loops (loop inside another loop)

output = ""
for x in range(0,5,1):
	for y in range(0, 5):
		if x == y:
			output += "*"
		else:
			output += " "
	output += "\n"
print output
'''





'''
#What is the output of the following code?

for x in range(4):
	print x, # output: 0 1 2 3 



for x in range(3):
	print "light", # output: light light light


	
i = 0
while i < 0:
	i += 5
print i # output: 0



count = 0
for num in range(5,10):
	if num%2==0:
		count+=1
print str(num) + ":" + str(count) #output: 9:2
								  #this is because num stops at 9; doesn't go to 10 because false
'''
num		num <10		T/F		new num		count
5		5<10		T		6			0
6		6<10		T		7			1
7		7<10		T		8			1
8		8<10		T		9			2
9		9<10		T		10			2
10		10<10		F
'''



x = 9
while x>5:
	y = x-5
	while y>0:
		print "*",
		y-=1
	x-=1
	print #moves to next line
	
	