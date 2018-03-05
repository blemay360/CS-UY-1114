input_num=int(input("Enter decimal number: "))
num=input_num
num_M=num//1000
num=num%1000
num_D=num//500
num=num%500
num_C=num//100
num=num%100
num_L=num//50
num=num%50
num_X=num//10
num=num%10
num_V=num//5
num=num%5
num_I=num
roman=(num_M*"M")+(num_D*"D")+(num_C*"C")+(num_L*"L")+(num_X*"X")+(num_V*"V")+(num_I*"I")
print(roman)
