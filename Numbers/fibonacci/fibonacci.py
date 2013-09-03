#!/usr/bin/python

import sys

quiet= False;
all= False;
for arg in sys.argv:
	if(arg == "--quiet"):
		quiet= True
	if(arg == "--all"):
		all= True
	if(arg[0] == '-'):
		if("q" in arg):
			quiet= True
		if("a" in arg):
			all= True

if not(quiet):
	sys.stdout.write("Program to find the nth Fibonacci number.\nEnter n: ")
user_input= sys.stdin.readline()

def validate(n):
	try:
		n= int(n)
		if n < 0:		
			sys.exit("" if quiet else "n must be non-negative")
	except ValueError:
		sys.exit("" if quiet else "n must be an integer")

validate(user_input)
n= int(user_input)

def fib(n):
	if n == 0:
		return [0]
	elif n == 1:
		return [0, 1]
	else:
		result= [0, 1]
		first= 0
		second= 1
		for i in range(2, n + 1):
			temp= second
			second= first + second
			first= temp
			result.append(second)
		return result

fib_n= fib(n)
print(fib_n)


