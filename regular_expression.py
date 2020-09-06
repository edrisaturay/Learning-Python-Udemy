# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 15:08:33 2020

@author: edris
"""
import re

pattern = re.compile('search this')
string = 'search this inside of this test please'

match = pattern.search(string)
match2 = pattern.findall(string)
match3 = pattern.fullmatch(string)
match4 = pattern.match(string)
print ( match4 )