#!/usr/bin/python

import sys

quiet= False; #True to suppress messages
all= False; #True to print all fib numbers up to n
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

#ensures n is a non-negative integer
def validate(n):
	try:
		n= int(n)
		if n < 0:		
			sys.exit("" if quiet else "n must be non-negative")
	except ValueError:
		sys.exit("" if quiet else "n must be an integer")

validate(user_input)
n= int(user_input)

#returns a list of the fibonacci numbers from 0 to n
#runs interatively in O(n) time
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

if all:
	for fib in fib_n:
		sys.stdout.write(str(fib) + " ")
	sys.stdout.write("\n")
else:
	sys.stdout.write(str(fib_n[-1]) + "\n")



