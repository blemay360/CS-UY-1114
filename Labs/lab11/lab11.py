#!/usr/bin/python3
class Calendar:
	def __init__(self):
		self.to_do_list = ToDoList()
#		input_date=input("Please enter today's date in mm/dd/yy format: ")
		date='4/20/18'
		date=date.split('/')
		self.__month=int(date[0]);
		self.__day=int(date[1]);
		self.__year=int(date[2]);
		self.__day_names=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
#		self.__day_num=int(input("Please enter the day of the week today (1 for Monday and 7 for Sunday): "));
		self.__day_num=5;

	def start_new_day(self):
		self.__day+=1;
		if ((self.__month == 1) or (self.__month == 3) or (self.__month == 5)or (self.__month == 7)or (self.__month == 8)or (self.__month == 10)or (self.__month == 12)) and (self.__day > 31):
			self.__day %= 31;
			self.__month+=1;
		elif (self.__month == 2) and (self.__day > 28):
			self.__day %= 28;
			self.__month+=1;
		elif ((self.__month == 4) or (self.__month == 6) or (self.__month == 9) or (self.__month == 11)) and (self.__day > 30):
			self.__day %= 30;
			self.__month+=1;
		if self.__month > 12:
			self.__month=self.__month % 12
			self.__year+=1;
		self.__day_num+=1;
		if self.__day_num > 7:
			self.__day_num=self.__day_num % 7;
		print(self);

	def __repr__(self):
		return("\nToday's date is: "+str(self.__day_names[self.__day_num-1])+' '+str(self.__month)+'/'+str(self.__day)+'/'+str(self.__year)+'\n'+str(self.to_do_list))




class ToDoList:
	def __init__(self):
		self.__to_do=[];
		self.__to_done=[];
	def create_to_do_list_item(self):
		task=input("Enter the activity: ")
		self.__to_do.append(task);
	def check_to_do_list(self):
		for i in range(len(self.__to_do)):
			if (input("Did you "+str(self.__to_do[i])+'? (y/n) ') == 'y'):
				self.__to_done.append(self.__to_do[i]);
		for i in self.__to_done:
			if i in self.__to_do:
				self.__to_do.remove(i);
		print("\nUpdated To-Do List:\n"+str(self))
	def __repr__(self):
		return("\nToday's accomplishment\n=========================\n"+print_nicely(self.__to_done)+'\nThings Left To Do\n=========================\n'+print_nicely(self.__to_do))




def print_nicely(lst):
	output=''
	for i in lst:
		output+=i+'\n'
	return(output)




def main():
	calendar = Calendar()
	while True:

		print("\nMain Menu:")
		print("1. Create New Calendar") 
		print("2. Add To-Do List Item")
		print("3. Check Off To-Do List")
		print("4. Show Today's Calendar")
		print("5. Start the Next Day\n")
		
		answer = input("What would you like to do? ")
		if answer == '1':
			calendar = Calendar()
		elif answer == '2':
			calendar.to_do_list.create_to_do_list_item()
		elif answer == '3':
			calendar.to_do_list.check_to_do_list()
		elif answer == '4':
			print(repr(calendar))
		elif answer == '5':
			calendar.start_new_day()




if __name__=="__main__":
	main()
