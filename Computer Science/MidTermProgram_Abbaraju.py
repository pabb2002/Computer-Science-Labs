#Pranav Abbaraju
#December 15th, 2017
#Mid Term Program

def cycles(firstCycle, secondCycle, thirdCycle, midTerm):
	print "Cycle1: " + str(firstCycle) + "; " "Cycle2: " + str(secondCycle) + "; " + "Cycle3: " + str(thirdCycle) + "; " + "Midterm: " + str(midTerm)

def midTerm(firstCycle, secondCycle, thirdCycle, midTerm):
	semesterPts = (firstCycle/7)+(secondCycle/7)+(thirdCycle/7)+(midTerm/14)
	semesterGrd = int(semesterPts*2)
	output = "\rSemester points: " + str(semesterPts) + "\rYour semester average is: " + str(semesterGrd)
	return output

cycles(100, 100, 98, 100)
print ""
print midTerm(float(raw_input("Enter your cycle 1 grade --> ")), float(raw_input("Enter your cycle 2 grade --> ")), float(raw_input("Enter your estimated cycle 3 grade --> ")), float(raw_input("Enter your Mid Term grade --> ")))
