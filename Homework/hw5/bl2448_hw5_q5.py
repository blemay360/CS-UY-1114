password=input("Enter a password: ")
upper_count=0
lower_count=0
digit_count=0
special_count=0
if (len(password) >= 8):
	for letter in range(len(password)):
		if password[letter].isupper():
			upper_count+=1
		elif password[letter].islower():
			lower_count+=1
		elif password[letter].isdigit():
			digit_count+=1
		elif ("!@#$".find(password[letter]) != -1):
			special_count+=1
if (upper_count >= 2) and (lower_count >= 1) and (digit_count >= 2) and (special_count >= 1):
	print(password, "is a valid password.")
else:
	print(password, "is not a valid password.")
