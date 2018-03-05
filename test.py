#!/usr/bin/python3
base=input("Please enter base pairs: ")
complimentary=''
for i in range(len(base)):
	if i>0 and i%4==0:
		complimentary+=' '
	c = base[i]
	c=c.lower()
	if (c == 'g'):
		complimentary+='C'
	elif (c == 'c'):
		complimentary+='G'
	elif (c == 'a'):
		complimentary+='T'
	elif (c == 't'):
		complimentary+='A'
	else:
		print("Break out the Head & Shoulders")
		break
print(complimentary)
