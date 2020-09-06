# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 02:49:18 2020

@author: edris
"""

def fib(num):
    
    a = 0
    b = 1
    
    for item in range(num):
        yield a
        
        temp  = a
        
        a = b
        b = temp + b
        
for x in fib(20):
    print(x)