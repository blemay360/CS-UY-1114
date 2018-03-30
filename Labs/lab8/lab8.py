#!/usr/bin/python3


#Problem 1:
def consecutiveChars(ch,n):
	string=''
	for i in range(n):
		count = ord(ch) + i;
		if count > 122:
			count-=26;
		string += chr(count);
	return(string);

print(consecutiveChars('x', 6));



#Problem 2:
def anagramTest(a, b):
	if (len(a) > len(b)):
		return False;
	b=list(b);
	for char in a:
		if (a.count(char) > b.count(char)):
			return False;
	return True
print(anagramTest('abcdefg','gfedcba'));



#Problem 3: 
def encodeBinary(str_in):
	count=1;
	for i in range(len(str_in)-1):
		if str_in[i] == str_in[i+1]:
			count+=1;
		else:
			print(count, str_in[i]);
			count=1;
		if (i == len(str_in)-2):
			print(count, str_in[len(str_in)-1]);
encodeBinary('0010000111111');



#Problem 4:
def counter(myInt, n):
	output=[]
	for i in range(n):
		output.append(myInt+i);
	return(output);

print(counter(10,5));



#Problem 5:
def count(lst, item):
	return(lst.count(item));
print(count([0,32,'a','0','4',15,'q','0'],'0'));



#Problem 6:
def power(n):
	output=[]
	for i in range(1,n+1):
		output.append(2**i);
	return(output);
print(power(7));



#Problem 7:
def altFind(masterString, substring, start, end):
	for i in range(start,end-start+1):
		if (masterString[start+i:start+i+len(substring)] == substring):
			return(i+start);
	return(-1);

print(altFind("This is a string to search with a bunch of material to search through", 'string', 10, 10));

#abcdefabcdef #cde  #0#10


def multi_find(masterString, substring, start, end):
	output=[];
	for i in range(start,end-start+1):
		index=altFind(masterString, substring, i, i);
		if (index != -1):	
			output.append(index);
			#i=index+len(substring)
	return(output);

print(multi_find("How much wood would a woodchuck chuck if a woodchuck could chuck wood?", 'chuck', 0, 60));

