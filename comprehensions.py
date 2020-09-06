# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 02:31:20 2020

@author: edris
"""

#list, set, dictionary


#List
myList  = [item for item in 'hello']

myList2 = [item for item in range(0, 100)]

myList3 = [item * 2 for item in range(0, 100)]

myList4 = [item ** 2 for item in range(0, 100) if item % 2 == 0]

#Set
mySet = {item for item in 'hello'}

#Dictionary
simpleDict = {
    'a': 1, 
    'b': 2
}
myDict = {key : value**2 for key, value in simpleDict.items() if value % 2 == 0}
myDict2 = {item: item * 2 for item in [1,2,3]  }

print(myDict2)