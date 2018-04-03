def encode(raw_str):
	encoded_list=[];
	char_list=[];
	count=1;
	for i in range(len(raw_str)-1):
		if (raw_str[i] == raw_str[i+1]):
			count+=1;
		else:
			char_list.append(raw_str[i]);
			char_list.append(count);
			encoded_list.append(char_list);
			char_list=[];
			count=1;
		if (i == len(raw_str)-2):
			char_list.append(raw_str[len(raw_str)-1]);
			char_list.append(count);
			encoded_list.append(char_list);
	return(encoded_list)

def decode(encoded_lst):
	plain_txt=""
	for i in range(len(encoded_lst)):
		for j in range(encoded_lst[i][1]):
			plain_txt+=encoded_lst[i][0];
	return(plain_txt);

def main():
	raw_string='aadccccaa'
	encoded=encode(raw_string);
	print(encoded);
	print(decode(encoded));

if __name__=="__main__":
	main();
