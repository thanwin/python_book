# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:17:01 2018

@author: Than Win
"""
#Inheritance Example
class fGrandFather():
    fGFMoney = 1000
    
class father(fGrandFather):
    fMoney = 500

class mGrandFather():
    mGFMoney = 800
    
class mother(mGrandFather):
    mMoney = 300
    
class son(father, mother):
    money = 100

sonObj = son()

print ('My own money ...$ ', sonObj.money)    
print ('Money inherited from my father ...$ ', sonObj.fMoney)    
print ('Money inherited from my mother ...$ ', sonObj.mMoney)    
print ('Money inherited from my grand father (father side...$ ', sonObj.fGFMoney)
print ('Money inherited from my grand father (mother side...$ ', sonObj.mGFMoney)
