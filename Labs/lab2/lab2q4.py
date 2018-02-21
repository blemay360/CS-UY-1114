#!/usr/bin/python3
num=int(input("Please input a number less than 100: "))
fifties=num // 50
num=num-fifties*50
tens=num // 10
num=num-tens*10
fives=num // 5
num=num-fives*5
ones=num
print((fifties*"L")+(tens*"X")+(fives*"V")+(ones*"I"))
