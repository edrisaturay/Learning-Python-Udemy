# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:00:23 2020

@author: edris
"""

def checkDriverAge(age = 0): 
    if int(age) < 18:
        return 'Sorry, you are too young to drive this car. Powering off'
    elif int(age) > 18:
        return 'Powering on. Enjoy the ride!'
    elif int(age) == 18: 
        return 'Congratulations on your first year of driving. Enjoy the ride!'
        

age = input('What is your age: ')
print(checkDriverAge(age))