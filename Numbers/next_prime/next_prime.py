#!/usr/bin/python

import sys

#writes 2 to start, special case as only even number

primes= [2] #list to hold all currently generated primes
sys.stdout.write("2")

#returns if n is prime
def is_prime(n):
	for prime in primes:
		if n % prime == 0:
			return False
	return True;

n= 3 #first odd prime
while True:
	if is_prime(n):
		primes.append(n)
		sys.stdout.write(" " + str(n))
	n += 2 #no more primes will be evem

