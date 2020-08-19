# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:48:17 2020

@author: edris
"""

isMagician = False
isExpert = True

# Check if magican AND expert:  "you are a master magician" 
# Check if magician but not expert: "atleast you're getting there" 
# if you're not a magician: "You need magic powers" 

if isExpert and isMagician: 
    print('You\'re a master magician')
elif isMagician and not(isExpert): 
    print('atleast you\'re getting there')
elif not(isMagician) : 
    print ('you need magic powers')