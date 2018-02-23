import turtle, random
#Program 1
n=int(input("Please input a number: "))
for i in range(1, n+1):
	for j in range(1, i+1):
		print(j, end='')
	print()

#Program 2
n=int(input("Please enter a number: "))
for i in range(1, n+1):
	print((n-i)*"."+i*str(i))

#Program 3
first_num=int(input("Please enter the first number: "))
second_num=int(input("Please enter the second number: "))
distance=0
for i in range(len(str(first_num)),-1,-1):
	if (first_num // (10**i) != second_num // (10**i)):
		distance+=1
	first_num=first_num % (10**i)
	second_num=second_num % (10**i)
print(distance)

#Program 4
n=int(input("Please enter a number: "))
angle_sum=(n-2)*180
for i in range(n):
	turtle.forward(100)
	turtle.right(180-(angle_sum / n))
turtle.done()

#Program 5
target=random.randint(1, 100)
print("I thought of a number between 1 and 100!")
guess=0
while(guess != target):
	guess=int(input("Try to guess what it is: "))
	if(target == guess):
		print("Congrats! You guessed my number!")
	elif(target < guess):
		print("Wrong guess. My number is smaller than yours")
	else:
		print("Wrong guess. My number is bigger than yours")
