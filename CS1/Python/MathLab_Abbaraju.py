# Pranav Abbaraju
# Math Lab

x = int(raw_input("Enter an integer for x:: "))
y= int(raw_input("Enter an integer for y:: "))
z = float(raw_input("Enter a decimal for z:: "))

productXy = x*y
productXyz = x*y*z
remainderX = x%2
remainderY = y%2
remainderZ = z%2

print "Product of x and y is " + str(productXy)
print "Product of x, y, and z is " + str(productXyz)
print str(x) + " mod 2 is " + str(remainderX)
print str(y) + " mod 2 is " + str(remainderY) 
print str(z) + " mod 2 is " + str(remainderZ)