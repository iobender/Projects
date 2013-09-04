#!/usr/bin/python

import sys

primes= [2]
sys.stdout.write("2")

def is_prime(n):
	for prime in primes:
		if n % prime == 0:
			return False
	return True;

n= 3
while True:
	if is_prime(n):
		primes.append(n)
		sys.stdout.write(" " + str(n))
	n += 2

