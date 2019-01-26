# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 13:04:53 2018

@author: Than Win
"""
#Test class
class rectangle:
    width = 0.0
    height = 0.0
    
    def area(self):
        return self.width * self.height

rec = rectangle()
rec.width = 5.2
rec.height = 3.2
print (rec.area())
