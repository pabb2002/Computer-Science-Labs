# Pranav Abbaraju
# If Statements Lab 2


#Mini IfLab2_01:

def legalAge(age):
	if age >= 16:
		print "At age", age, "a person is old enough to drive"
		if age >= 18:
			print "At age", age, "a person is old enough to vote"
			if age >= 21:
				print "At age", age, "a person is old enough to drink alcohol legally"
			else:
				print "At age", age, "a person is not old enough to drink alcohol legally"
		else:
			print "At age", age, "a person is not old enough to vote"
			print "At age", age, "a person is not old enough to drink alcohol legally"
	else:
		print "At age", age, "a person is not old enough to drive"
		print "At age", age, "a person is not old enough to vote"
		print "At age", age, "a person is not old enough to drink alcohol legally"
		
legalAge(int(raw_input("Enter your age:: ")))
legalAge(int(raw_input("Enter your age:: ")))
legalAge(int(raw_input("Enter your age:: ")))
legalAge(int(raw_input("Enter your age:: ")))


#Mini IfLab2_02:

def longDivision(num1,num2):
	if num1 > num2:
		if num1%num2 != 0:
			print num1, "divided by", num2, "equals", num1//num2, "remainder", num1%num2
		else:
			print num1, "divided by", num2, "equals", num1//num2 
	elif num2 > num1:
		if num2%num1 != 0:
			print num2, "divided by", num1, "equals", num2//num1, "remainder", num2%num1
		else:
			print num2, "divided by", num1, "equals", num2//num1
	else:
		print num2, "divided by", num1, "equals 1"

longDivision(int(raw_input("Enter a whole number:: ")), int(raw_input("Enter another whole number:: ")))



#Mini IfLab2_03:

def phoneCall(time):
	if time > 5:
		additionalCost = (time-5)*.65
		print "A", time, "minute phone call to Lubbock, TX costs $" + str(additionalCost+2.45)
	else:
		print "A", time, "minute phone call to Lubbock, TX costs $2.45"

phoneCall(int(raw_input("Enter the number of minutes your phone call lasted:: ")))



#Mini IfLab2_04:

def nameAndGrade(name, grade):
	if grade >= 90:
		print str(name) + ", you made a grade of " + str(grade) + ". Great job!!"
	elif grade >= 70 and grade < 90:
		print str(name) + ", you made a grade of " + str(grade) + ". Good job, work a little bit harder."
	else: 
		print str(name) + ", you made a grade of " + str(grade) + ". Study more and you will do better." 
		
nameAndGrade(raw_input("Enter your name:: "), int(raw_input("Enter your grade:: ")))	  	