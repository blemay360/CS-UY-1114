n=int(input("Please input a positive integer n: "))
for i in range(1,n+1):
	print((n-i)*" ", end='')
	for j in range(1,i+1):
		print(j, end='')
	print()
