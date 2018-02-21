weight=float(input("Please enter weight in kilograms: "));
height=float(input("Please enter height in meters: "));
BMI=(weight/height**2);
print("BMI is:", BMI);
print("According to the CDC, this BMI is ", end='')
if (BMI < 18.5):
	print("underweight")
elif (BMI < 25):
	print("normal")
elif (BMI < 30):
	print("overweight")
else:
	print("obese")
