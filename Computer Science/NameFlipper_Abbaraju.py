# Pranav Abbaraju
# Name Flipper

def nameFlipper(name):
	return name[name.find(" ")+1:len(name)] + "," + " " + name[0:name.find(" ")]
print nameFlipper("Pravav Abbaraju")
print nameFlipper("Nathaniel Feuntes")
print nameFlipper("Ryan Gallagher")
print nameFlipper("Daneilla Leeber")
print nameFlipper("Jessica Oleskey")
print nameFlipper("Luis Villegas")
print nameFlipper("Brandon Wilson")