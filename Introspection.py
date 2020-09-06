# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 19:31:23 2020

@author: edris

Inspecting an object
"""


class User: 
    
    def __init__(self, email): 
        self._email = email
        
    def signIn(self): 
        print('Logged in ')
        
        
class Wizard(User): 
    def __init__(self, name, power, email): 
        User.__init__(self, email)
        self._name = name
        self._power = power
        
    def attack(self): 
        print(f'Attacking with power of {self._power}')
        
        
merlin = Wizard('Merlin', 90, 'merlin@gmail.com')

print(dir(merlin))