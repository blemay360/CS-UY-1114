def find_all(lst,val):
	output=[];
	for i in range(len(lst)):
		if (lst[i] == val):
			output.append(i);
	return(output);
