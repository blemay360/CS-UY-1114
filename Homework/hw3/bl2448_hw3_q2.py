firstPrice=float(input("Enter price of first item: "))
secondPrice=float(input("Enter price of second item: "))
card=input("Does customer have a club card? [y/n] ")
tax=float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))
print("Base price =", firstPrice + secondPrice)
if (firstPrice < secondPrice):
	firstPrice=firstPrice*.5
else:
	secondPrice=secondPrice*.5
if (card == "y" or card == "Y"):
	discountPrice=(firstPrice+secondPrice)*.9
else:
	discountPrice=firstPrice+secondPrice
print("Price after discounds =", round(discountPrice, 2))
print("Total price =", round(discountPrice*(1+(tax/100)), 2 ))
