#!/usr/bin/python

import sys

quiet= False;
for arg in sys.argv:
	if(arg == "--quiet"):
		quiet= True
	if(arg[0] == '-'):
		if("q" in arg):
			quiet= True

if not(quiet):
	sys.stdout.write("Program to find all prime factors of n.\nEnter n: ")
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

def is_prime(n):
	if n == 0 or n == 1 or n == 2:
		return True
	elif n % 2 == 0:
		return False
	else:
		for i in range(3, n, 2):
			if n % i == 0:
				return False
		return True

factors= []
i= 2
limit= n ** .5
while i <= limit:
	if is_prime(i):
		if n % i == 0:
			factors.append(i)
			n /= i
			i -= 1
	i += 1
if not n == 1:
	factors.append(n)



print factors

