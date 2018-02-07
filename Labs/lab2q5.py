#!/usr/bin/python3
birthday=int(input("Please enter a date of birth: "))
date=int(input("Please enter today's date: "))
birthdayYear=birthday//10000
birthdayMonth=(birthday//100)%100
birthdayDay=birthday%100

dateYear=date//10000
dateMonth=(date//100)%100
dateDay=date%100

print("Date of birth is "+str(birthdayMonth)+"/"+str(birthdayDay)+"/"+str(birthdayYear))
print("Today's date is "+str(dateMonth)+"/"+str(dateDay)+"/"+str(dateYear))

totalDaysAlive=((dateYear*365)+(dateMonth*30)+dateDay)-((birthdayYear*365)+(birthdayMonth*30)+birthdayDay)
yearsAlive=totalDaysAlive//365
monthsAlive=(totalDaysAlive % 365) // 30
daysAlive=(totalDaysAlive % 365) % 30
print("You have been alive for " + str(yearsAlive) + " years, " + str(monthsAlive) + " months, and " + str(daysAlive) + " days")
