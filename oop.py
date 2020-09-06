# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 00:15:11 2020

@author: edris
"""

class PlayerCharacter:
    
    membership = True
    
    def __init__(self, name): 
        self.name = name
        
    def run(self): 
        print('run')
        
    @classmethod 
    def addingThings(cls, num1, num2): 
        return num1 + num2
    
        
player1 = PlayerCharacter('Edrisa')



print(player1.name)

class Cat: 
    species = 'mammal'
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    @classmethod
    def adding_things(cls, a, b): 
        return cls('Teddy', 2,3)
    
    @staticmethod 
    def addingNumbers(a, b): 
        return a+b
    
    def run(self): 
        return self
    
    def speak(self):
        print(f'My name is {self.name}, and i am {self.age} years old')
    
    
        
cat1 = Cat('Garfield', '2')
cat2 = Cat('Puss', '3')
cat3 = Cat('Lofy', '1')


print(cat1.speak())

def findOldestCat(*args):
    return max(args)
    
# print(findOldestCat(cat1.age, cat2.age, cat3.age))