# Pranav Abbaraju
# MathTrick Lab

def trick1(num):
	num01 = num
	num = num*2
	num = num+6
	num = num/2
	num = num - num01
	return num
		
print "Your answer is " + str(trick1(int(raw_input("Enter a number less than 10:: "))))

# The trick1(num) method uses a user-inputted value to run through a series of
#reassignments of the parameter to return the value of 3 regardless of the 
#number inputted by the user as long as it is under 10 


def trick2(num2):
	num1 = num2
	num2 = num2*3
	num2 = num2+45
	num2 = num2*2
	num2 = num2//6
	num2 = num2 - num1
	return num2
	
print "Your answer is " + str(trick2(int(raw_input("Enter a number:: "))))

# The trick2(num) method also uses a user-inputted value to run through a 
#series of reassignments of the parameter.
#It returns the value of 15 regardless of the number inputted by the user  