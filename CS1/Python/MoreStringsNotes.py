# Strings loops and find/rfind methods

# Why do we use loops with string?
# to go index by index through the string 

# this way is long
s = "first"
print s[0]
print s[1]
print s[2]
print s[3]
print s[4]

# but with a loop:
s = "first"
for x in range(len(s)): #range => start to stop, does range run at the stop? No
	print s[x],
print 

for x in range(len(s)-1, -1, -1): #must start at len(s) - 1 because length is one greater than highest index
								  #stop value is -1 because check is if x>-1, so that the x reaches index of 0
	print s[x],
print 

for let in s: #can't manipulate step and direction; let is letter and you don't need brackets to access each letter
	print let,
print 



# find method starts at 0 and increases by 1 until it finds the character or phrase
happy = "happys days"
print len(happy)
print happy.find("a")
print happy.find("ys")
print happy.find("x") # -1 tells that it is not part of the string bc no index of -1
print happy.find(" ")

# rfind method starts at len()-1 and decreases by 1 until it finds the character or phrase
print happy.rfind("a")
print happy.rfind("ys")
print happy.rfind("x") # still returns -1
print happy.rfind(" ")

#count 
print happy.count("a")
print happy.count("ys")




