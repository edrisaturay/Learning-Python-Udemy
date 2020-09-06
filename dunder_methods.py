# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 19:34:19 2020

@author: edris
"""

class Toy: 
    def __init__(self, color, age): 
        self._color = color
        self._age = age
        
    def __str__(self):
        return f'{self._color}'
        
actionFigure = Toy('red', 0)

print(actionFigure.__str__())