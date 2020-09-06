# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 01:27:21 2020

@author: edris

generate a sequence of values

"""

def makeList(n): 
    result = []
    for i in range(n): # range is a generator
        result.append(i*2)
        
    return result

myList = makeList(100)


def generatorFunction(): 
    for i in range(1000000): 
        yield i 
        
for item in generatorFunction():
    print(item)