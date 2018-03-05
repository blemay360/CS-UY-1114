roman=input("Enter number in the simplified Roman system: ")
total=0
for letter in range(len(roman)):
	if (roman[letter] == "M"):
		total+=1000
	elif (roman[letter] == "D"):
		total+=500
	elif (roman[letter] == "C"):
		total+=100
	elif (roman[letter] == "L"):
		total+=50
	elif (roman[letter] == "X"):
		total+=10
	elif (roman[letter] == "V"):
		total+=5
	elif (roman[letter] == "I"):
		total+=1
print(roman, "is", total)
