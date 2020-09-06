# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 19:51:15 2020

@author: edris
"""

class SuperList(list): 
    def __len__(self):
        return 100
    
superList = SuperList()

print(superList.__len__())

superList.append(5)
print(superList[0])