expression=input("Enter a mathematical expression: ")
oprand1=expression[0:expression.find(" ")]
oprand2=expression[expression.rfind(" ")+1: len(expression)]
op=expression[expression.find(" ")+1: expression.rfind(" ")]
if (op == "+"):
	print(expression, "=", int(oprand1)+int(oprand2))
elif (op == "-"):
	print(expression, "=", int(oprand1)-int(oprand2))
elif (op == "/"):
	print(expression, "=", int(oprand1)/int(oprand2))
else:
	print(expression, "=", int(oprand1)*int(oprand2))
