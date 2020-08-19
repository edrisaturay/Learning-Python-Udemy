# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:56:20 2020

@author: edris
"""
# is check if the location in memory where the value is stored is the same

print(True == 1) # True
print('' == 1) # False
print([] == 1) # False
print(10 == 10.0) # True
print([] == []) # True

print(True is 1) # False
print('' is 1) # False
print([] is 1) # False
print(10 is 10.0) # False
print([] is []) # True
