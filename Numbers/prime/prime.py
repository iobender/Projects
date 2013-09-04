#!/usr/bin/python

import sys

quiet= False; #True to suppress messages
for arg in sys.argv:
	if(arg == "--quiet"):
		quiet= True
	if(arg[0] == '-'):
		if("q" in arg):
			quiet= True

if not(quiet):
	sys.stdout.write("Program to find all prime factors of n.\nEnter n: ")
user_input= sys.stdin.readline()

#tests if n is a non-negative integer
def validate(n):
	try:
		n= int(n)
		if n < 0:		
			sys.exit("" if quiet else "n must be non-negative")
	except ValueError:
		sys.exit("" if quiet else "n must be an integer")

validate(user_input)
n= int(user_input)

#returns if n is prime (considers 0 and 1 prime for simplicity)
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

factors= [] #list to hold all factors
i= 2 #first viable prime
limit= n ** .5 #necessary limit to check for factors is sqrt(n)
while i <= limit:
	if is_prime(i): 
		if n % i == 0: #n is divisible by this prime
			factors.append(i)
			n /= i
			i -= 1 #reset i to same
	i += 1
if not n == 1: #remaining number
	factors.append(n)
#can be sped up by first getting all 2's, then only checking odds


#prints compact version of factorization, with a^x * b * c^z
i= 0
while i < len(factors):
	counter= 1
	while counter + i < len(factors) and factors[i] == factors[i + counter]:
		counter += 1
	sys.stdout.write(str(factors[i]) + ("" if counter == 1 else "^" + str(counter)))
	i= i + counter
	if not i == len(factors):
		sys.stdout.write(" * ")
sys.stdout.write("\n")

