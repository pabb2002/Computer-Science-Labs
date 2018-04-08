# Pranav Abbaraju
# Loops forward and backward, nested loops

# a loop that moves forward starts low ends high (+ step)
# a loop that moves backward starts high ends low (- step)
'''
def forwardLoop():
	output = ""
	for x in range(1, 10, 2): # range() with 3 parameters: 3rd parameter is the step
		output += str(x) + "\n"
	return output
print forwardLoop()

def backwardsLoop():
	output = ""
	for x in range(10, 0, -3): 
		output += str(x) + "\n"
	return output
print backwardsLoop()

def reLoop():
	output = ""
	for x in reversed(range(1,5)):# another way to go backward: however, it starts at 4 because it is the same process
		output += str(x)
	return output
print reLoop()





# Nested loops: create things using rows and columns
# loop inside a loop
for x in range(5):
	print "Outer Loop " + str(x) + ": ",
	for y in range(5):
		print str(y),
	print "\n"
'''
output = ""
for x in range(5):  #outer loop controls number of rows
	for y in range(5):  #inner loop controls number of columns 
		output += "*"   #reassignment
	output += "\n"		#everything inside the outer loop is the action
print output
	

