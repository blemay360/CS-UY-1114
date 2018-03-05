char=input("Enter a character: ")
num=ord(char)
if (num >= 97) and (num <= 122):
	print(char, "is a lower case number.")
elif (num >= 65) and (num <= 90):
	print(char, "is an upper case number.")
elif (num >= 48) and (num <= 57):
	print(char, "is a digit.")
else:
	print(char, "is a non-alphanumeric character.")
