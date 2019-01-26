# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:09:30 2018

@author: Than Win
"""
#module test
import os
root_dir = "C:/Users/kvm/"
cur_dir = root_dir + '/python_test/'
os.chdir(cur_dir)

import fibo
fibo.fib(1000)
print()
print (fibo.fib2(100))

os.chdir(root_dir)
