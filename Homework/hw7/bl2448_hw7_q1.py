#!/usr/bin/python3
import random

def create_permutation(n):
	lst=[];
	for i in range(n):
		lst.append(i);
	for i in range(n):
		temp=lst[i];
		randint=random.randint(0,n-1);
		lst[i]=lst[randint];
		lst[randint]=temp;
	return(lst);

def scramble_word(word):
	output='';
	rand_lst=create_permutation(len(word));
	for i in range(len(word)):
		output+=word[rand_lst[i]];
	return(output);

def main():
	file_read=open('hw7 - word bank.txt', 'r');
	counter=0;
	for line in file_read:
		counter+=1;
	file_read.close();
	file_read=open('hw7 - word bank.txt', 'r');
	counter=0;
	rand_int=random.randint(1,100);
	for line in file_read:
		counter+=1;
		if counter == rand_int:
			word=line[0:len(line)-1]; #len(line)-1 gets rid of the newline character
	print("Unscramble the word: ", end='');
	for char in scramble_word(word):
		print(char,end=' ');
	print();
	attempt=input("Try #1: ")
	counter=1
	while attempt != word and counter < 3:
		print("Wrong!");
		counter+=1;
		attempt=input("Try #"+str(counter)+': ');
	if attempt == word:
		print("Yay you got it!");
	else:
		print("Better luck next time");
	file_read.close();

if __name__=="__main__":
	main()
