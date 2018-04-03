def create_prefix_lists(lst):
	output=[];
	for i in range(len(lst)+1):
		temp_lst=[];
		for j in range(i):
			temp_lst.append(lst[j]);
		output.append(temp_lst);
	return(output);

lst=[2,4,6,8,10];
print(create_prefix_lists(lst));
