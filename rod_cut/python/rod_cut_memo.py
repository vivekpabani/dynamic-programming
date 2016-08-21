#!/usr/bin/env python


"""
Problem Definition :
Cut Rod (Top Down - Memoization)
"""

__author__ = 'vivek'


def rod_cut(p, n):
    r = [-1 for i in range(n+1)]
    
    return rod_cut_aux(p, n, r)


def rod_cut_aux(p, n, r):

    if r[n] >= 0:
        return r[n]
    
    if n == 0:
        q = 0
    else:
        q = -1
    
        for i in range(1, n+1):
            q = max(q, p[i] + rod_cut_aux(p, n-i, r))
    
    r[n] = q
    
    return q


def main():
	
	p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
	n = 4

	print(rod_cut(p, n))
	
	
if __name__ == "__main__":
	main()
