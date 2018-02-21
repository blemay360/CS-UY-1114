length=int(input("Please enter the length of the sequence: "))
print("Please enter your sequence:")
total=0
for i in range(0, length):
	total+=int(input())
print("The geometric mean is:", round(total**(1/length), 4))
