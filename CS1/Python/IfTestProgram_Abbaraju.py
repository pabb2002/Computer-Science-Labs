# Pranav Abbaraju
# If Test Program

def speeding(speedLimit, speed, school):
	if speed >= speedLimit:
		speedDifference = speed - speedLimit
		if speedDifference > 30:
			ticket = (6*speedDifference) + 75 + 160
		else:
			ticket = (6*speedDifference) + 75
		if school == "Y":
			ticket = ticket*2 
		print "Ticket amount: $" + str(ticket)
	elif speed < speedLimit:
		print "Ticket amount: $0"

speeding(int(raw_input("What is the posted speed limit? ")), int(raw_input("How fast was the car taveling in mph? ")), raw_input("Did the violation occur in a school zone? (Y/N) "))