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

