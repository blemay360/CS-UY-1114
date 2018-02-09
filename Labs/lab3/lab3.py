#Problem 1a
language=input("Enter a language: ")
if (language=="en"):
	print("Hello, world!")
elif (language=="es"):
	print("Hola mundo!")
else:
	print("Unrecognized language")

#Problem 1b
num=int(input("Enter a number: "))
if (num%2==1):
	print("Odd")
else:
	print("Even")

#Problem 2
name=input("Please enter your name: ")
gradYear=int(input("Please enter your graduation year: "))
currentYear=int(input("Please enter current year: "))
if (gradYear <= currentYear):
	print(name, "graduated")
elif (currentYear+1 == gradYear):
	print(name, "is a senior")
elif (currentYear+2 == gradYear):
	print(name, "is a junior")
elif (currentYear+3 == gradYear):
	print(name, "is a sophomore")
elif (currentYear+4 == gradYear):
	print(name, "is a freshman")
else:
	print(name, "is not in college yet")

#Problem 3
leg1=int(input("Please enter the first leg: "))
leg2=int(input("Please enter the second leg: "))
hypotenuse=float(input("Please enter the hypotenuse: "))
if (abs((leg1**2+leg2**2)-hypotenuse**2) <= 0.05):
	print(str(leg1) + ", " + str(leg2) + " and " + str(hypotenuse) + " form a right triangle.")
else:
	print (str(leg1) + ", " + str(leg2) + " and " + str(hypotenuse) + " do not form a right triangle.")

#Problem 4
a=int(input("Please enter a: "))
b=int(input("Please enter b: "))
if (a==0 and b==0):
	print("The equation has infinite solutions")
elif (a==0):
	print("The equation has no solutions")
else:
	print("The equation has a single solution and x =", (-b)/a)

#Problem 5
weightPounds=int(input("Please enter a weight in pounds: "));
weightKilos=weightPounds*(0.45);
weightOunces=weightPounds*16;
print (weightPounds, "pounds is equivalent to", weightOunces, "ounces and", weightKilos, "kilograms")

#Problem 6
numSides=int(input("Enter the number of sides: "))
if (numSides==3):
	print("The shape is a triangle")
elif (numSides==4):
	equalSides=input("Are the sides equal? (Y/N): ")
	rightAngles=input("Are the angles 90 degrees? (Y/N): ")
	if (equalSides=="Y" and rightAngles=="Y"):
		print("The shape is a square")
	elif (equalSides=="Y" and rightAngles=="N"):
		print("The shape is a parallelogram")
	elif (equalSides=="N" and rightAngles=="Y"):
		print("The shape is a rectangle")
	elif (equalSides=="N" and rightAngles=="N"):
		print("The shape is a quadrilateral")
	else:
		print("Unknown input")
elif (numSides==5):
	print("The shape is a pentagon")
else:
	print("Unknown shape")

#Program 7
time=int(input("Please enter time in 24 hr format: "));
hourInput=time//100;
if (hourInput > 12):
	hourOutput=hourInput%12;
else:
	hourOutput=hourInput
minute=time%100;
if (hourInput >= 12 and minute <= 9):
	print(str(hourInput) + ":0" + str(minute) + " in 12 hr format is: " + str(hourOutput) + ":0" + str(minute) + "pm")
elif (hourInput >= 12 and minute > 9):
	print(str(hourInput) + ":" + str(minute) + " in 12 hr format is: " + str(hourOutput) + ":" + str(minute) + "pm")
elif (hourInput < 12 and minute <= 9):
	if (hourInput == 0):
		print(str(hourInput) + ":0" + str(minute) + " in 12 hr format is: 12:0" + str(minute) + "pm")
	else:
		print(str(hourInput) + ":" + str(minute) + " in 12 hr format is: " + str(hourOutput) + ":0" + str(minute) + "am")
else:
	if (hourInput == 0):
		print(str(hourInput) + ":" + str(minute) + " in 12 hr format is: 12:" + str(minute) + "pm")
	else:
		print(str(hourInput) + ":" + str(minute) + " in 12 hr format is: " + str(hourOutput) + ":" + str(minute) + "am")
