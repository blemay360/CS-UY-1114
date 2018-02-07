print("Please enter your amount in the format of dollars and cents in two separate lines:")
dollars=int(input(""))
cents=int(input(""))
total=(dollars*100)+cents
quarters=total//25
total=total-(25*quarters)
dimes=total//10
total=total-(10*dimes)
nickels=total//5
total=total-(5*nickels)
pennies=total
print(dollars, "dollars and", cents, "cents are:")
print(quarters, "quarters,", dimes, "dimes,", nickels, "nickels and", pennies, "pennies")
