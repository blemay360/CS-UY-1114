def sort_file(filename):
	dict_out={};
	file_in=open(filename,"r");
	header=file_in.readline();
	for line in file_in:
		lst=line.split(",");
		train_line=lst[0][0];
		stop=lst[2];
		if train_line not in dict_out:
			dict_out[train_line]=[];
			dict_out[train_line].append(stop);
		elif stop not in dict_out[train_line]:
			dict_out[train_line].append(stop);
	return(dict_out);

def main():
	line_stops=sort_file("hw8 - mta train stop data.csv");
	usr_input=input("Please enter a train stop, or 'done' to stop: ")
	while usr_input != 'done':
		if usr_input in line_stops:
			print(usr_input, "line: ", end='');
			for i in range(len(line_stops[usr_input])):
				if i < len(line_stops[usr_input])-1: 
					print(line_stops[usr_input][i], end=', ')
				else:
					print(line_stops[usr_input][i])
			print();
		usr_input=input("Please enter a train stop, or 'done' to stop: ")

if __name__=="__main__":
	main();
