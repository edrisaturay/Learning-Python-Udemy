# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 23:12:05 2020

@author: edris
"""

someList = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for item in someList:
    if someList.count(item) > 1: 
        if item not in duplicates:
            duplicates.append(item)
        
print(duplicates)