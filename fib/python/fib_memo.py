#!/usr/bin/env python


"""
Problem Definition :

Fibonaci with Memoization (Top Down)

"""

__author__ = 'vivek'


def fib(n, lookup):
	
	if n == 0 or n == 1:
		lookup[n] = n
	
	if lookup[n] is None:
		lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)
	
	return lookup[n]
	

def main():
	
	lk = [None for i in range(20)]
	
	print(fib(10, lk))
	

if __name__ == "__main__":
	main()
