day=input("Enter the day the call started at: ")
time=int(input("Enter the time the call started at (hhmm): "))
duration=int(input("Enter the duration of the call (in minutes): "))
if (day == "Sat" or day == "Sun"):
	cost=duration*.15
elif (time < 800 or time > 1800):
	cost=duration*.25
else:
	cost=duration*.4
print("This call will cost $"+str(cost)) 
