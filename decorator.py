# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 23:45:31 2020

@author: edris
"""
from time import time

def myDecorator(func): 
    def wrapperFunction(*args, **kwargs):
        print('**************')
        func(*args, **kwargs)
        print('**************')
    return wrapperFunction


    
@myDecorator
def hello(greeting, emoji): 
    print(greeting)
    

def performance(func): 
    def wrapperFunction(*args, **kwargs): 
        start  = time()
        
        result = func(*args, **kwargs)
        
        end = time()
        
        print(f'took {(end - start)} seconds')
        return result
        
    return wrapperFunction

@performance
def longTime(): 
    for i in range(1000000000): 
        i*5
        
longTime()