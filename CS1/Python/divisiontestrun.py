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