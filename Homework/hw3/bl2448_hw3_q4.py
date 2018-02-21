import math
a=float(input("Enter value of a: "))
b=float(input("Enter value of b: "))
c=float(input("Enter value of c: "))
if (a == 0 and b == 0 and c == 0):
	print("This equation has an infinite number of solutions")
elif (a == 0 and b == 0):
	print("This equation has no solution")
elif ((b**2-4*a*c) < 0):
	print("This equation has no real solutions")
elif ((b**2-4*a*c) == 0):
	print("This equation has one real solution: ", end='')
	print((-b+math.sqrt(b**2-4*a*c))/(2*a))
else:
	print("This equation has two real solutions: ", end='')
	print((-b+math.sqrt(b**2-4*a*c))/(2*a), "and ", end='')
	print((-b-math.sqrt(b**2-4*a*c))/(2*a), end='')
