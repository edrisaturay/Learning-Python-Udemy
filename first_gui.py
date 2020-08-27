# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 22:54:56 2020

@author: edris
"""

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

fill = '$'
empty = ' '
for row in picture:
    for pixel in row:
        if(pixel):
            print(fill, end="")
        else:
            print(empty, end ="")
    print("")