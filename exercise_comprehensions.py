# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 02:49:51 2020

@author: edris
"""

someList = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']

duplicates = {item for item in someList if someList.count(item) > 1 }

print(duplicates)