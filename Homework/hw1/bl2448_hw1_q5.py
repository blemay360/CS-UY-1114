print("Please enter number of coins:")
quarters=int(input("# of quarters: "))
dimes=int(input("# of dimes: "))
nickels=int(input("# of nickels: "))
pennies=int(input("# of pennies: "))
total=(25*quarters)+(10*dimes)+(5*nickels)+(1*pennies)
dollars=total//100
cents=total%100
print("The total is", dollars, "dollars and", cents, "cents")
