# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:17:01 2018

@author: Than Win
"""
#Inheritance Example
class grandFather():
    gfMoney = 1000
    
class father(grandFather):
    fMoney = 500

class son(father):
    money = 100

sonObj = son()

print ('My own money ...$ ', sonObj.money)    
print ('Money inherited from my father ...$ ', sonObj.fMoney)    
print ('Money inherited from my grand father ...$ ', sonObj.gfMoney)
