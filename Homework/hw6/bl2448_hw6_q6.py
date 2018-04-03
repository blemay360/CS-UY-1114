def main():
	lst1 = [1, 2, 3, 4, 5, 6];
	rev_lst1 = reverse_to_new_list(lst1);
	print("After reverse_to_new_list, lst1 is", lst1, "and the returned list is", rev_lst1);
	
	lst2 = [1, 2, 3, 4, 5, 6];
	print("Before reverse_in_place, lst2 is", lst2);
	reverse_in_place(lst2);
	print("After reverse_in_place, lst2 is", lst2);

def reverse_to_new_list(lst):
	rev_lst1=[]
	for i in range(len(lst)-1,-1,-1):
		rev_lst1.append(lst[i]);
	return(rev_lst1);

def reverse_in_place(lst):
	for i in range(len(lst)//2):
		temp=lst[i];
		lst[i]=lst[len(lst)-i-1];
		lst[len(lst)-i-1]=temp;
	return(lst);

if __name__=="__main__":
	main();
