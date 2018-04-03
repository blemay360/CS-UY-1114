def max_abs_val(lst):
	max_val=abs(lst[0]);
	for i in lst:
		if (abs(i) > max_val):
			max_val=abs(i);
	return(max_val);

def main():
	lst=[-19,-3,20,-1,0,-25];
	print(max_abs_val(lst));

if __name__=="__main__":
	main();
