def add_list(lst1, lst2):
	#Adds two lists and returns the summed list
	sum_lst=[];
	for i in range(len(lst1)):
		sum_lst.append(lst1[i]+lst2[i]);
	return(sum_lst);

def take_input(lst):
	#Takes input from user, and adds it to a list
	#List is ended by typing 'done'
	print("Input list elements. Type 'done' to end list");
	usrIn=input();
	while (usrIn != 'done'):
		lst.append(int(usrIn));
		usrIn=input();
	return(lst);

def print_lst(lst):
	#Takes a list and prints it out, element by element
	for i in lst:
		print(i);

def main():
	lst1=[];
	lst2=[];
	take_input(lst1);
	take_input(lst2);
	if (len(lst1)==len(lst2)):
		print_lst(add_list(lst1,lst2));
	else:
		print("Lists are different lengths");

if __name__=="__main__":
	main();
