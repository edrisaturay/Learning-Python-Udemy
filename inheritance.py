# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:59:58 2020

@author: edris
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
    
class Archer(User): 
    def __init__(self, name, arrows, email): 
        super().__init__(email)
        self._name = name
        self._arrows = arrows
        
    def attack(self): 
        print(f'Attacking with arrows: arrows left  - {self._arrows}')
        self._arrows -= 1
        

merlin = Wizard('Merlin', 80, 'merlin@gmail.com')
robin = Archer('Robin', 100, 'robin@gmail.com')

print(merlin._email)