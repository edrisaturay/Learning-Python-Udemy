# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 01:13:07 2020

@author: edris
"""
from collections import Counter, defaultdict, OrderedDict

import datetime
from array import array

li = [1,2,3,4,5,6,7,7]
print(Counter(li))

dictionary = defaultdict(lambda:0,{'a': 1, 'b': 2})

print(dictionary['c'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

dict1 = {}
print (d2 == d)


print(datetime.time(5,45,3))
print(datetime.date.today())

arr = array('i', [1,2,3])
print (arr)