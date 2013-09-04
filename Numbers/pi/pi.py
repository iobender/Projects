#!/usr/bin/python

import sys

quiet= False;
for arg in sys.argv:
	if(arg == "-q" or arg == "--quiet"):
		quiet= True
if not(quiet):
	sys.stdout.write("Program to find the first n digits of pi.\nEnter n: ")
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

result= 0
for i in range(n + 1):
	step= (4/(8*i + 1) - 2/(8*i + 4) - 1/(8*i + 5) - 1/(8*i + 6))
	print(str(i) + ": " + str(step))
	result += step
print(result)

