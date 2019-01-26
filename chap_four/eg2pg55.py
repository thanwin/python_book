# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:47:39 2018

@author: Than Win
"""

print ('This is the example 2 from Mathematics Grade 11, page 55')
print ('Find the sqeuence whose first term is 1 and Un = 2Un - 1')
Un = 1
print ('Answer is : 1', end=', ')
for n in range(3):
    print (2*Un, end=', ')
    Un = 2*Un
print ('...')
