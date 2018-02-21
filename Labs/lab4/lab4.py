#Problem 1
a=input("Please enter string a: ")
b=input("Please enter string b: ")
if (len(a) > len(b)):
	shortVar=b
	longVar=a
else:
	shortVar=a
	longVar=b
print(str(shortVar)+str(longVar)+str(shortVar))

#Problem 3
dividend=int(input("Please enter the dividend: "))
divisor=int(input("Please enter the divisor: "))
i=0
total=divisor
while (total <= dividend):
	total+=divisor
	i+=1
print("Quotient of", dividend, "divided by", divisor, "is:", i)

#Problem 4
dividend=int(input("Please enter the dividend: "))
divisor=int(input("Please enter the divisor: "))
total=dividend
while (total >= divisor):
	total-=divisor
print("Remainder of", dividend, "divided by", divisor, "is:", total)

#Problem 5
n=int(input("Please input n: "))
cubes=1
counter=2
while (cubes < n):
	print(cubes)
	cubes=counter**3
	counter+=1
