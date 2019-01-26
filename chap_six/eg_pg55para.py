# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 17:04:42 2018

@author: Than Win
"""
#Function example with parameter pass and parameter return
def eg1pg55(param):
    """
    This is the example 1 from Mathematics Grade 11, page 55.
    This program prints the first four terms of the sqeuence whose general term Un = n + 3
    """
    print ('This is the example 1 from Mathematics Grade 11, page 55')
    print ('Find the first four terms of the sqeuence whose general term Un = n + 3')
    ans = []
    for n in range(1,param):
        ans.append(n+3)
    return(ans)
    
def eg2pg55(param):
    """
    This is the example 2 from Mathematics Grade 11, page 55.
    This program prints the sqeuence whose first term is 1 and Un = 2Un - 1
    """
    print ('This is the example 2 from Mathematics Grade 11, page 55')
    print ('Find the sqeuence whose first term is 1 and Un = 2Un - 1')
    Un = 1
    ans = []
    ans.append(Un)
    for n in range(param):
        ans.append(2*Un)
        Un = 2*Un
    return(ans)
    
print ('Answer is : ', eg1pg55(5)) 
print()
print ('Answer is : ', eg2pg55(3))    
