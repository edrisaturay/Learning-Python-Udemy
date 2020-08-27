# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 23:19:46 2020

@author: edris

def - is used to define a function
"""

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
def showTree():
    fill = '$'
    empty = ' '
    for row in picture:
        for pixel in row:
            if(pixel):
                print(fill, end='')
            else:
                print(empty, end ='')
        print("")
        
# With Arguments

def sayHello(name='Darth Vader', emoji=':-('):
    print(f'Hello {name}{emoji}')
    
## Positional  Arguments
sayHello('Edrisa', ':-)')

## Keyword Arguments
sayHello(emoji=':-)', name='Edrisa')

## Default arguments
sayHello()



"""
Return

"""

def sum(num1, num2): 
    return num1 + num2
    
print(sum(4,5))