daysJohn=int(input("Please enter the number of days John has worked: "));
hoursJohn=int(input("Please enter the number of hours John has worked: "));
minutesJohn=int(input("Please enter the number of minutes John has worked: "));
daysBill=int(input("Please enter the number of days Bill has worked: "));
hoursBill=int(input("Please enter the number of hours Bill has worked: "));
minutesBill=int(input("Please enter the number of mintues Bill has worked: "));

minutesTotal=((daysJohn*24*60+daysBill*24*60)+(hoursJohn*60+hoursBill*60)+(minutesJohn+minutesBill));

daysBoth=minutesTotal//(60*24);
minutesTotal=minutesTotal%1440;
hoursBoth=minutesTotal//60;
minutesBoth=minutesTotal%60;
print("The total time both of them worked together is:", daysBoth, "days,", hoursBoth, "hours and", minutesBoth, "minutes.");
