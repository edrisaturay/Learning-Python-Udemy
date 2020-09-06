# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 18:56:50 2020

@author: edris
"""

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Lofy(Cat): 
    def sing(self, sounds): 
        return f'{sounds}'
    
myCats = [
    Simon('Simon', 2), Sally('Sally', 3), Lofy('Lofy', 4) 
]

pets = Pets(myCats)

print(pets.walk())