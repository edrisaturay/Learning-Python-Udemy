# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 01:32:29 2020

@author: edris
"""
from functools import reduce

myList = [1,2,3,4,5]
yourList = [10,20,30]

#Map
def multiplyBy2(data): 
    return data*2
print(list(map(multiplyBy2, myList))) 

#Filter
def odd(data): 
   return data % 2 != 0
print(list(filter(odd, myList)))

#Zip
print(list(zip(myList, yourList)))

#reduce
def accumulator(acc, data): 
    return acc + data
print(reduce(accumulator, myList, 0))