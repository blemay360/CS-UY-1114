n=int(input("Please enter a positive integer n: "))
for i in range (1, n+1):
	if ((i//10)%2 == 0) and (i%2 == 0):
		print(i)
