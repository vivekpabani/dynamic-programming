#!/usr/bin/env python


"""
Problem Definition :
Cut Rod (Bottom Up - Tab)
"""

__author__ = 'vivek'


def rod_cut(p, n):
    r = [-1 for i in range(n+1)]
    r[0] = 0
    q = -1
    for j in range(1, n+1):
        q = -1
        for i in range(1, j+1):
            q = max(q, p[i] + r[j-i])
        r[j] = q
    return q

def main():
	
	p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
	n = 4

	print(rod_cut(p, n))
	
	
if __name__ == "__main__":
	main()
