# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 14:08:00 2020

@author: edris
"""

from translate import Translator
'''
myFile = open('name.txt')

sentence = myFile.readline()

translator = Translator(to_lang='ja')

translation = translator.translate(sentence)

print ( translation )
'''

try: 
    with open('name.txt', mode='r') as myFile: 
        sentence = myFile.readline()

        translator = Translator(to_lang='ja')

        translation = translator.translate(sentence)

        print ( translation )
    
except FindNotFoundError as e: 
    print('check your file path silly')