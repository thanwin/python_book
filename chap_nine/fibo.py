# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:03:05 2018

@author: Than Win
"""
# Fibonacci numbers module
def fib(n):
    """Print a Fibonacci series up to n."""
    a,b = 0, 1
    while b < 1000:
        print(b, end=' ')
        a,b = b, a+b
        
def fib2(n):
    """return Fibonacci series up to n."""
    result = []
    a,b = 0, 1
    while b < 1000:
        result.append(b)
        a,b = b, a+b
    return(result)        
