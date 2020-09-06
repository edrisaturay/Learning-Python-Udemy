# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 04:05:28 2020

@author: edris
"""

def multiply(*args):
    product = 1
    for item in args:
        product *=  item
        
    return product

