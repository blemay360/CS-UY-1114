import random
target=random.randint(1,100)
print("I thought of a number between 1 and 100! Try to guess it.\n")
tries=5
high_guess=100
low_guess=0
counter=1
guess=101
while(counter <= tries) and (guess != target):
	print("Range: ["+str(low_guess)+", "+str(high_guess)+"], Number of guesses left: "+str(tries-counter+1))
	guess=int(input("Your guess: "))
	if (guess == target):
		print("Congrats! You guessed my number in", counter, "guesses.")
	elif (counter == tries):
		print("Out of guesses! My number is", target)
	elif (guess > target):
		print("Wrong! My number is smaller.\n")
		if (guess < high_guess):
			high_guess=guess
	else:
		print("Wrong! My number is bigger.\n")
		if (guess > low_guess):
			low_guess=guess
	counter+=1
	
