#Pranav Abbaraju

name = "Pranav" #name is the reference variable
print name[2]
print name[4]
#slicing => [:] => used to access a section of string
print name[0:3]
#The stopping point (4 in this case) is not displayed
print name[0:1]
print name[1:1]
print name[:-2]
print name[3:-1]
		   
#string methods

print len(name)
print name.find("a")
r = "r"
print name.rfind(r)

y = raw_input("Enter a word: ")
z = ""
def returnWord(y, z):
	for x in range(len(y)):
		z += y[x]
	print z
returnWord(y, z)