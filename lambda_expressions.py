# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 02:16:35 2020

@author: edris

lambda param: action
"""

from functools import reduce

myList = [1,2,3,4,5]


print(list(map(lambda item: item*2, myList))) 

print(reduce(lambda acc, item: acc + item, myList))


myList = [5,4,3]

print(list(map(lambda item: pow(item, 2), myList)))


a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda x: x[1])

print(a)