'''
#Program 1:
print("Program 5:")
s=input("Please enter a string: ")
s2=''
for letter in range(len(s)):
	if s[letter].isupper():
		s2+=(s[letter].lower())
	elif s[letter].islower():
		s2+=(s[letter].upper())
	else:
		s2+=s[letter]
print(s2)

#Program 2:
print("Program 2:")
str_a=input("Please enter string a: ")
str_b=input("Please enter string b: ")
if (len(str_a) > len(str_b)):
	print(str_b + str_a + str_b)
else:
	print(str_a + str_b + str_a)

#Program 3:
print("Program 3:")
s=input("Please enter string s: ")
k=int(input("Please enter a number k: "))
s=' '+s
output=''
for i in range((len(s) // k) + 1):
	if (i % 2 == 0):
		output+=s[(k*i)+k:(k*i):-1]
	else:
		output+=s[(k*i)+1:(k*i)+k+1]
print(output)

#Program 4:
print("Program 4:")
s=input("Please enter string s: ")
s=' '+s+' '
output=''
last_space=0
for char in range(len(s)):
	if (s[char] == ' '):
		output+=(s[char:last_space:-1])	
		last_space=char
print("Result:" + output)
'''
#Program 5:
print("Program 5:")
s=input("Please enter a string s: ")
output_substring=''
output_count=0
for i in range(len(s)):
	for j in range(i+2, len(s)):
		substring=(s[i:j])
		count=s.count(substring)
		if (count > output_count):
			output_count = count
			output_substring = substring
if (output_count > 1):
	print("The substring", output_substring, "repeated", output_count, "times in", s)
else:
	print("There are no repeating substrings in", s)
