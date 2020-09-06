# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 02:06:28 2020

@author: edris
"""

from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capPetNames(data): 
    return data.capitalize()

print(list(map(capPetNames, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def filterScores(data):
    return data > 50

print(list(filter(filterScores, scores)))
#4 Combine all of the numbers that are in a list on this file using reduce
# (my_numbers and scores). What is the total?

def accumulator(acc, data): 
    return acc + data

print(reduce(accumulator, (my_numbers + scores)))