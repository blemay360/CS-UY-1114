weightPounds=float(input("Please enter weight in pounds: "));
heightInches=float(input("Please enter height in inches: "));
weightKilos=(weightPounds*0.453592);
heightMeters=(heightInches*0.0254);
BMI=(weightKilos/heightMeters**2);
print("BMI is: ", BMI);
