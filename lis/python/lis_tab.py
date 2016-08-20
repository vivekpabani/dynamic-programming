#!/usr/bin/env python


"""
Problem Definition :

Length of Longest Increasing Subsequence (Bottom Up)

"""

__author__ = 'vivek'


def lis(arr):
    n = len(arr)
    
    lis_l = [1 for k in range(n)]
    
    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i] and lis_l[j] + 1 > lis_l[i]:
                lis_l[i] = lis_l[j] + 1
    
    return max(lis_l)


def main():
	
	num_l = [10, 22, 9, 33, 21, 50, 41, 60]
	
	print(lis(num_l))
	
	
if __name__ == "__main__":
	main()
