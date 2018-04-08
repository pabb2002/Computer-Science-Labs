# Pranav Abbaraju
# Discount

def discount(amount):
	if amount >= 2000: 
		amount = amount - .1*amount
	return amount
	
print discount(int(raw_input("Enter the sales amount:: ")))