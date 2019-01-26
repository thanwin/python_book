# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 16:27:46 2018

@author: Than Win
"""
#Function example without parameter pass
def eg1pg55():
    """
    This is the example 1 from Mathematics Grade 11, page 55.
    This program prints the first four terms of the sqeuence whose general term Un = n + 3
    """
    print ('This is the example 1 from Mathematics Grade 11, page 55')
    print ('Find the first four terms of the sqeuence whose general term Un = n + 3')
    print ('Answer is : ', end=' ')
    for n in range(1,5):
        print (n + 3, end=', ')
    print ('...')
    
def eg2pg55():
    """
    This is the example 2 from Mathematics Grade 11, page 55.
    This program prints the sqeuence whose first term is 1 and Un = 2Un - 1
    """
    print ('This is the example 2 from Mathematics Grade 11, page 55')
    print ('Find the sqeuence whose first term is 1 and Un = 2Un - 1')
    Un = 1
    print ('Answer is : 1', end=', ')
    for n in range(3):
        print (2*Un, end=', ')
        Un = 2*Un
    print ('...')
    
eg1pg55()
print()
eg2pg55()    
