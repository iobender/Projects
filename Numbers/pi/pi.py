#!/usr/bin/python

import sys

quiet= False;
for arg in sys.argv:
	if(arg == "-q" or arg == "--quiet"):
		quiet= True
if not(quiet):
	sys.stdout.write("Program to find the nth digit of pi\nEnter n: ")
user_input= sys.stdin.readline()

def valid_input(n):
	try:
		int(n)
		return True
	except ValueError:
		return False

if valid_input(user_input):
	n= int(user_input)
else:
	sys.exit("" if quiet else "n must be a number")

print(n)
