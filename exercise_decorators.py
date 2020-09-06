# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 00:33:31 2020

@author: edris
"""
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapperFunction(*args, **kwargs): 
        user = args[0]
        if user.get('valid') :
            return fn(*args, **kwargs)
        
    return wrapperFunction

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)