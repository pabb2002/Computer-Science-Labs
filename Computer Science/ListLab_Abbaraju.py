# 0 <--- Pranav Abbaraju, ListLab_Abbaraju
print "#Output for Python - List Lab\n"

# 1 <--- Make an empty list with a reference variable called subjects
subjects = []

#2 <--- Print out the empty list to see what is the output of an empty list: look at output document
print "#1 - #2"
print subjects
print 

#3 <--- Using the append method, add your class schedule into the list
subjects.append("Spanish 3 Pre-AP")
subjects.append("AP Macroeconomics")
subjects.append("Compsci Pre-AP")
subjects.append("Drawing 2")
subjects.append("Chemistry Pre-AP")
subjects.append("AP World History")
subjects.append("AP Statistics")
subjects.append("English 2 Pre-IB")  

#4 <--- Print out the list subject to see what the output is of a list with elements (items): look at output document
print "#3 - #4"
print subjects
print 

#5 <--- Using the remove method, remove your 3rd and 8th period classes
subjects.remove("Compsci Pre-AP")
subjects.remove("English 2 Pre-IB")

#6 <--- Print out the list to see what has happened to the list: look at output document
print "#5 - #6"
print subjects
print 

#7 <--- Using the pop method, remove your 1st and 5th period classes
subjects.pop(0)
subjects.pop(2)

#8 <--- Print out the list to see what has happened to the list: look at output document
print "#7 - #8"
print subjects
print 

#9 <--- Using the list reassignment/assignment, change the value of the remaining classes to say your A-day schedule
subjects[0] = "Spanish 3 Pre-AP"
subjects[1] = "AP Macroeconomics"
subjects[2] = "Compsci Pre-AP"
subjects[3] = "Drawing 2"

#10 <-- Print out the list to see what has happened to the list: look at output document
print "#9 - #10"
print subjects
print

#11 <--- Use the insert method to place your B-day classes in between your A-day classes
subjects.insert(1, "Chemistry Pre-AP")
subjects.insert(3, "AP World History")
subjects.insert(5, "AP Statistics")
subjects.insert(7, "English 2 Pre-IB")


#12 <--- Print out the list to see what has happened to the list: look at output document
print "#11 - #12"
print subjects
print

#13 <--- Using a loop print out your schedule in numeric order 1st to 8th
aDay = []
bDay = []
def order():
	for x in range (0, len(subjects), 2):
		print subjects[x]
	for x in range(1, len(subjects), 2):
		print subjects[x]
		
#!** <--- do not reorder your list, continue with the list in the order it is in

#14 <--- Print out your schedule in numeric order 1st to 8th: look at output document: look at output document
print "#13 - #14"
order()

#15 <--- Using a loop(s) print out a schedule you might get at the beginning of school, create a list called teachers that holds your teachers and then print your schedule: look at output document
print "Pranav Abbaraju"
def dashes():
	print "---------------------------------------------------------"
dashes()
print 
 

teachers = ["Beatriz Villalon", "Valerie Reyna", "Michelle Lux", "Mara Johnson-Petrinec", "Steven Payne", "Shawna Queen", "Chelsea Cason", "Jennifer Dyer"]
print "A-day schedule"
dashes()
dashes()
for x in range (0, len(subjects), 2):
	print "{:<40}{:1}".format(subjects[x], teachers[x])
	dashes()
print
print "B-day schedule"
dashes()
dashes()
for x in range(1, len(subjects), 2):
	print "{:<35}{:1}".format(subjects[x], teachers[x])
	dashes()