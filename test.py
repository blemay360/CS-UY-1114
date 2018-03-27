#!/usr/bin/python3
def main(val=0):
	if val==0: 
		return("Hello world");
	else:
		return("Hi universe");

if __name__=="__main__":
	print(main(int(input())));
