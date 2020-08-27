# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 22:48:42 2020

@author: edris
"""

# iterable - list, dictionary, tuple, set, string that can be iterated over. 
# iterated - one by one check each item in the collection 

user = {
    'name': 'Golem', 
    'age': 25, 
    'can_swim': False
}

for item in user: # print only keys
    print (item)
    
for item in user.items():
    print (item)
    
for item in user.values(): 
    print (item)
    
for item in user.keys(): 
    print (item)
    

for item in user.items(): 
    key, value = item # Tuple Unpacking
    print(key, value)
    
for key, value in user.items(): 
    print(key, value)