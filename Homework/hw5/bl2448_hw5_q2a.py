char=input("Enter a character: ")
if not char.isalnum():
	print(char, "is a non-alphanumeric character.")
elif char.isdigit():
	print(char, "is a digit.")
elif char.islower():
	print(char, "is a lower case letter.")
else:
	print(char, "is an upper case letter.")
