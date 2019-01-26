# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:07:39 2018

@author: Than Win
"""

a,b = 0, 1

while b < 1000:
    print(b)
    a,b = b, a+b
