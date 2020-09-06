# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 00:48:46 2020

@author: edris
"""
while True: 
    try: 
        age = int(input('What is your age: '))
        10/age
        print(age)
    except ValueError as valueError:  # Specify the error
        print('Please enter a number: ' + valueError)
    except ZeroDivisionError as zeroDivisionError: 
        print('Please enter age higher than 0' + zeroDivisionError)
    else: 
        print('Thank you...')
        break
    finally:
        print('OK. i am finally done..')
        
# Raising Errors

#raise ErrorName (raise ValueError)