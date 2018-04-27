#!/usr/bin/python3
#Problem 1:
def add_entry(phonebook,name,phone_number):
	if name not in phonebook:
		if check_phone(phone_number):
			phonebook[name]=phone_number;
		else:
			print("Number", phone_number, "is not valid");
	else:
		print(name,"is already in the phonebook");

def check_phone(phone_number):
	if (len(phone_number) == 10) and phone_number.isdigit():
		return True;
	else:
		return False;

def lookup(phonebook,name):
	if name in phonebook:
		print(phonebook[name]);
	else:
		print(name,'is not in phonebook');

def print_all(phonebook):
	for name in phonebook:
		print(name,phonebook[name]);

def main():
	phonebook={};
	phonebook_in='Lab12-phonebook.txt'
	file_read=open(phonebook_in,'r');
	for line in file_read:
		lst=line.split(',');
		lst[1]=lst[1].split(' ');
		name=lst[1][1]+' '+lst[0];
		phone_number=lst[1][2];
		add_entry(phonebook,name,phone_number[0:len(phone_number)-1]);
	interact(phonebook);
	
def interact(phonebook):
	add_entry(phonebook, 'Preston Moore', '64699736000');
	add_entry(phonebook, 'Preston Moore', '6469973600');
	add_entry(phonebook, 'Preston Moore', '6469973600');
	lookup(phonebook, 'Larry Page');
	lookup(phonebook, 'Linda Sellie');
	print_all(phonebook);

if __name__=='__main__':
	main();

input("Press enter to continue to problem 2: ");

#Problem 2:
class BankAccount:
	def __init__(self, account_number, balance):
		self.bank_account={}
		self.bank_account[account_number]=int(balance);
		self.account_number=account_number
	def deposit(self, deposit):
		self.bank_account[self.account_number]+=int(deposit);
	def withdraw(self, withdrawl):
		if self.bank_account[self.account_number]-withdrawl >= 0:
			self.bank_account[self.account_number]-=int(withdrawl);
		else:
			print('Insufficient balance. The current balance remained as $'+str(self.bank_account[self.account_number]));
	def __repr__(self):
		return('Current balance is: $'+str(self.bank_account[self.account_number]));

my_account=BankAccount('BOA123', 1000)
print(my_account);
my_account.deposit(100);
print(my_account);
my_account.withdraw(500);
print(my_account);
my_account.withdraw(999999);

input("Press enter to continue to problem 3: ");

#Problem 3:
import random

class Patron:
	def __init__(self, name):
		self.name=name
		self.library_account_number='None'
		self.borrowed_books=[];
	def add_library_account_number(self,account_number):
		self.library_account_number=account_number
	def add_borrowed_book(self,book):
		self.borrowed_books.append(book);
	def __repr__(self):
		return("Name: "+self.name+"\nLibrary Account Number: "+str(self.library_account_number)+'\n\nBorrowed books:\n'+print_borrowed_books(self)+'\n')

class Library:
	def __init__(self, name, location):
		self.name=name;
		self.location=location;
		self.patrons={};
		self.books={};
		self.taken_ids=[];
	def add_book(self, book):
		self.books[book]='Available';
	def lend(self, patron, book):
		if book in self.books and self.books[book] == 'Available':
			if check_patron(patron, self.patrons):
				self.books[book]='Checked Out';
				patron.add_borrowed_book(book);
			else:
				print(patron.name+" is not a patron of "+self.name)
		else:
			print(book, 'is not available');
	def add_patron(self, patron):
		new_id=get_new_id(self);
		self.patrons[new_id]=patron;
		patron.add_library_account_number(new_id);
	def __repr__(self):
		return('Name: '+self.name+'\nLocation: '+self.location+'\n\nAvailable Books:\n'+print_books(self.books)+'\nLibrary Patron Information:\n'+print_nicely(self.patrons));

def check_patron(patron, patron_dict):
	for id_num in patron_dict:
		if patron_dict[id_num]==patron:
			return(True);
	return(False);
		
def get_new_id(library):
	new_id=random.randint(10000,99999);
	if new_id not in library.taken_ids:
		library.taken_ids.append(new_id);
		return new_id;
	else:
		get_new_id();

def print_nicely(dictionary):
	output='';
	for key in dictionary:
		output+=str(dictionary[key]);
	return(output);

def print_books(dictionary):
	output='';
	for book in dictionary:
		if dictionary[book] == 'Available':
			output+=book+'\n';
	return(output);

def print_borrowed_books(patron):
	output='';
	if len(patron.borrowed_books) > 0:
		for book in patron.borrowed_books:
			output+=book+'\n';
		return(output)
	else:
		return('');

def main3():
	bk_library=Library("Brooklyn Public Library", "6 Metrotech Center");
	bk_library.add_book("Ender's Game");
	bk_library.add_book("Ender's Shadow");
	bk_library.add_book("Shadow of the Hegemon");
	bk_library.add_book("Ready Player One");
	bk_library.add_book("The Outsiders");
	bk_library.add_book("Flowers for Algernon");
	bob = Patron('Bob')
	print(bob.library_account_number)
	bk_library.add_patron(bob)
	print(bob.library_account_number)
	print(bk_library)
	shuyu = Patron('Shuyu')
	bk_library.lend(shuyu, "Flowers for Algernon")
	bk_library.add_patron(shuyu)
	bk_library.lend(shuyu, "Old Man’s War")
	bk_library.lend(shuyu, "Ender's Shadow")
	bk_library.lend(bob, "Ender's Shadow")
	print(bk_library)

main3();
