#!/usr/bin/python3
import random
#Problem 1:
def write_name(filename,first_name,last_name):
	file_write=open(filename,'w');
	print(first_name, last_name, file = file_write);
	file_write.close();

write_name("Problem1", "Charles", "Darwin");

#Problem 2:
def write_random_numbers(filename,n):
	file_write=open(filename,'w');
	for i in range(n):
		print(random.randint(1,100), file = file_write);
	file_write.close();

write_random_numbers("Problem2", 7);

#Problem 3:
def sum_column(filename):
	sum=0;
	file_read=open(filename,'r');
	for line in file_read:
		sum+=int(line);
	return sum;
	file_read.close();

print(sum_column("Problem2"));

#Problem 4:
def html_table_generator(lst,file_to_write_to):
	file_write=open(file_to_write_to,'w');
	print('<html>\n\t<table>', file	= file_write);
	for i in range(len(lst)):
		print('\t\t<tr>', file = file_write);
		for j in range(len(lst[i])):
			if (i == 0):
				print('\t\t\t<th>',lst[i][j],'</th>',sep='',file = file_write)
			else:
				print('\t\t\t<td>',lst[i][j],'</td>',sep='',file = file_write)
		print('\t\t</tr>',file = file_write);
	print('\t</table>\n</html>', file = file_write);
	file_write.close();

lst=[['Header1', 'Header2', 'Header3', 'Header4',], ['R1C1', 'R1C2', 'R1C3', 'R1C4'], ['R2C1', 'R2C2', 'R2C3', 'R2C4'], ['R3C1', 'R3C2', 'R3C3', 'R3C4']];
html_table_generator(lst, "Problem4");
