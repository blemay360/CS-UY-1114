side1=float(input("Length of first side: "))
side2=float(input("Length of second side: "))
side3=float(input("Length of third side: "))
if (side1 == side2 and side1 == side3):
	print(str(side1) + ", " + str(side2) + ", " + str(side3) + " form an equilateral triangle")
elif (side1 == side2):
	if (abs(side1**2 + side2**2 - side3**2) <= 0.00001):
		print(str(side1) + ", " + str(side2) + ", " + str(side3) + " form an isosceles right triangle")
	else:
		print(str(side1) + ", " + str(side2) + ", " + str(side3) + " form an isosceles triangle")
else:
	print(str(side1) + ", " + str(side2) + ", " + str(side3) + " form a triangle that is neither isosceles nor equilateral")
