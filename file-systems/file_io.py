# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 01:33:14 2020

@author: edris
"""

myFile = open('test.txt')

print(myFile.readline())

#myFile.seek(0)
print(myFile.readline())

#myFile.seek(0)
print(myFile.readline())

'''
modes
r => read
w => write - create a new file if it doesn't exist
r+ => readwrite (overwrite at the cursor)
a => append
'''
with open('test.txt', mode='a') as myFile:
    text = myFile.write('hello')
    
    print(text)