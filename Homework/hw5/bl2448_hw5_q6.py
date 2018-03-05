string_in=input("Please enter a string of lowercase letters: ")
increasing=1
for letter in range(len(string_in)-1):
	if (ord(string_in[letter]) <= ord(string_in[letter+1])) and (increasing == 1):
		increasing=1
	else:
		increasing=0
if (increasing == 1):
	print(string_in, "is increasing.")
else:
	print(string_in, "is not increasing.")
