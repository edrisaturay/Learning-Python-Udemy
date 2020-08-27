# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:54:00 2020

@author: edris
"""

evenNumbers = [10,2,3,4,8,11]

def highestEven(numbers):
    even  = []
    for item in numbers: 
        if item % 2 == 0 : 
            even.append(item)
    return  max(even)


x = int(4)
y = float(2.9)

print (y)

print('helo'[0])

print(highestEven(evenNumbers))