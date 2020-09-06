# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:32:23 2020

@author: edris
"""

class User: 
            
    def signIn(self): 
        print('Logged in ')
        
        
class Wizard(User): 
    def __init__(self, name, power): 
        self._name = name
        self._power = power
        
    def attack(self): 
        print(f'Attacking with power of {self._power}')
    
class Archer(User): 
    def __init__(self, name, arrows): 
        self._name = name
        self._arrows = arrows
        
    def attack(self): 
        print(f'Attacking with arrows: arrows left  - {self._arrows}')
        self._arrows -= 1
        
    def checkArrows(self): 
        print(f'{self._arrows} remaining')
        
    def run(self):
        print('ran really fast')
        
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

edrisa = HybridBorg('Edrisa', 50, 10)

print(edrisa.checkArrows())