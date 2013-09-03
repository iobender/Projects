#!/usr/bin/python

import sys

quiet= False;
for arg in sys.argv:
	if(arg == "-q" or arg == "--quiet"):
		quiet= True

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

