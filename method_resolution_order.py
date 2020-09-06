# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:41:57 2020

@author: edris
"""

class A(): 
    num = 10
    
class B(A): 
    pass

class C(A): 
    num = 1
    
class D(B, C): 
    pass

    

class X: pass
class Y: pass
class Z: pass
class A(X, Y): pass
class B(Y, Z): pass
class M(B, A, Z): pass

print(M.__mro__)