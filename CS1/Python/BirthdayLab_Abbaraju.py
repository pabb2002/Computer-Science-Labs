# Pranav Abbaraju
# Birthday Lab
 
var = int(raw_input("Enter your birth month as a number:: "))
month = var
var = var + 18
var = var*25
var = var - 333
var = var*8
var = var - 554
var = var // 2
day = int(raw_input("Enter your birth date:: "))
var = var + day
var = var*5
var = var + 692
var = var*20
year = raw_input("Enter your birth year:: ")
var = var + int(year[2:4])
var = var - 32940
 
print var
 
if month == 1:
        	month = "January"
elif month == 2:
        	month = "February"
elif month == 3:
        	month = "March"
elif month == 4:
        	month = "April"
elif month == 5:
        	month = "May"
elif month == 6:
        	month = "June"
elif month == 7:
        	month = "July"
elif month == 8:
        	month = "August"
elif month == 9:
        	month = "September"
elif month == 10:
        	month = "October"
elif month == 11:
        	month = "November"
elif month == 12:
        	month = "December"
 
print str(month), str(day) + ",", str(year)