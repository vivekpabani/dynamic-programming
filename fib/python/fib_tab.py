#!/usr/bin/env python


"""
Problem Definition :

Fibonaci with Tabulation (Bottom Up)

"""

__author__ = 'vivek'


def fib(n):
	
	fib_l = [0 for i in range(n+1)]
	fib_l[1] = 1
	
	for j in range(2, n+1):
	    fib_l[j] = fib_l[j-1] + fib_l[j-2]
	
	return fib_l[n]
	

def main():
	
	print(fib(10))
	
	
if __name__ == "__main__":
	main()
