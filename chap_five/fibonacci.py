# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 16:04:16 2018

@author: Than Win
"""
# Write Fibonacci series up to n
def fib(n):
    """Print a Fibonacci series up to n."""
    a,b = 0, 1
    while b < 1000:
        print(b, end=' ')
        a,b = b, a+b
        
fib(1000)
