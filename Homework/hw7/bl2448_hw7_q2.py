#!/usr/bin/python3
'''

Brandon LeMay
CS 1114
bl2448

'''


# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):
	read_file=open(complete_weather_filename, 'r');
	write_file=open(cleaned_weather_filename, 'w');
	print('City,Date,High,Low,Precipitation',file=write_file);
	label=read_file.readline();
	for line in read_file:
		lst=line[0:len(line)-1].split(',');
		if lst[8].isalpha() == True:
			print(lst[0],lst[1],lst[2],lst[3],'0',sep=',',file=write_file)
		else:
			print(lst[0],lst[1],lst[2],lst[3],lst[8],sep=',',file=write_file)
	read_file.close();
	write_file.close();

# Part B
def f_to_c(f_temperature):
    return (f_temperature-32)*(5/9)

def in_to_cm(inches):
    return (inches/0.394)

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
	read_file=open(imperial_weather_filename, 'r');
	write_file=open(metric_weather_filename, 'w');
	print('City,Date,High,Low,Precipitation',file=write_file);
	label=read_file.readline();
	for line in read_file:
		lst=line[0:len(line)-1].split(',');
		print(lst[0],lst[1],f_to_c(int(lst[2])),f_to_c(int(lst[3])),in_to_cm(float(lst[4])),sep=',',file=write_file)
	read_file.close();
	write_file.close();


# Part C
def print_average_temps_per_month(city, weather_filename, unit_type):	
	read_file=open(weather_filename,'r');
	label=read_file.readline();
	high_averages=[0,0,0,0,0,0,0,0,0,0,0,0];
	low_averages=[0,0,0,0,0,0,0,0,0,0,0,0];
	months=[['January',0],['February',0],['March',0],['April',0],['May',0],['June',0],['July',0],['August',0],['September',0],['October',0],['November',0],['December',0]];
	for line in read_file:
		lst=line[0:len(line)-1].split(',');
		lst[1]=lst[1].split('/');
		if lst[0] == city:
			high_averages[int(lst[1][0])-1]+=float(lst[2]);
			low_averages[int(lst[1][0])-1]+=float(lst[3]);
			months[int(lst[1][0])-1][1]+=1
	print("\nAverage temperatures for ",city,':\n',sep='');
	for i in range(12):
		high_averages[i]=high_averages[i] / months[i][1];
		low_averages[i]=high_averages[i] / months[i][1];
		if unit_type == 'imperial':
			print(months[i][0],': ',high_averages[i],'F High, ',low_averages[i],'F Low',sep='');
		else:
			print(months[i][0],': ',high_averages[i],'C High, ',low_averages[i],'C Low',sep='');
	read_file.close();

# Part D
#How many days did New York have precipitation while the low was below 32F?
def possible_snow(city, weather_filename):
	read_file=open(weather_filename, 'r');
	label=read_file.readline();
	counter=0;
	for line in read_file:
		lst=line[0:len(line)-1].split(',');
		if float(lst[4]) != 0 and city == lst[0] and int(lst[3]) < 32:
			counter+=1;
	print("There were",counter,"days on record with a chance for snow");
	read_file.close();	

def main():
    print ("Running Part A")
    clean_data("weather.csv", "weather in imperial.csv")
    
    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")
    
    print ("Running Part C")
    print_average_temps_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_average_temps_per_month("New York", "weather in metric.csv", "metric")
    print_average_temps_per_month("San Jose", "weather in imperial.csv", "imperial")

    print ("Running Part D")
    possible_snow('New York', "weather in imperial.csv");

    
main()
