print("Please enter a non-empty sequence of positive integers, each one in a separate line. End your sequence by typing 'done':")
total=0
counter=0
num=input()
while (num != 'done'):
	total+=int(num)
	counter+=1
	num=input()
print("The geometric mean is:", total**(1/counter))
