# Pranav Abbaraju
# Loops

# What is the purpose of a loop?
	# a loop is a statement that will repeat other coding statements

# How many loops are in python?
	# There are two loops in python: for and while

# There are four things needed to make a loop:
	# 1. start
	# 2. check (what keeps the loop running; as long as it is true, loop runs)
	# 3. action
	# 4. step (movement in a loop)




'''
# syntax of a for loop statement:
for x in range(2):  # 'for' and 'in' are reserved words; python is the only one that can use them
					# 'x' is the loop control variable
					# in this case, what is its starting value? => 0
					# when range has only one parameter, starting value is always 0
					# 'in' takes into account the values from 0 to the stop ()
					# loops cannot run with negative range because 0 is not in the range
					# what direction is the loop going? => positive direction
					# 'range()' is the step (+1) and the check (x < 2)
	print x # this print is the action: the code that gets repeated
	

for i in range(7,10): #range with 2 parameters: start (7), check (i < 10)
	print i
for i in range(0,10):
	print i
for i in range(10):
	print i
for i in range(-5,10):
	print i
for i in range(-10,-5): 
	print i
'''



'''
#syntax for a while loop statement 
x = 1 # loop control variable, it will be used in the condition and the step of the while loop
	  # same as x in the for loop, but you have to declare it in while loops
while x >= 5: # while is a reserved word
			 # x >= 5 is the check or condition of the loop, must be true, runs until false
	print x # action of the loop
	x -= 2 # step, movement through the loop, must be declared as well
		   # while allows you to start anywhere, move multiple steps, positive or negative,
		   # but for loops only move 1 step in the positive direction
'''




# Using a for loop, print out the following one at a time: *****
# What are the four things neede for a loop?
	# 1. start: 0	2. check: range()	3. action	4. step range() + 1 

star = ""
for x in range(5):  # x: loop control variable, changes in the loop
					# range() is a method that acts like a condition
	star += "*"
print star

star = ""
y = 0 # or y = 1, then check would be y < 6 or y <= 5 
while y < 5:
	star += "*"
	y += 1
print star 