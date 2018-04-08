# Pranav Abbaraju
# Name Flipper

def nameFlipper(name):
	return name[name.find(" ")+1:len(name)] + "," + " " + name[0:name.find(" ")]
print nameFlipper(raw_input("Enter your full name: "))