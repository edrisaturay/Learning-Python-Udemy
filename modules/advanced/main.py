from utility import multiply
from shopping.cart import buy
import random
import pyjokes


myList = [1,2,3,4,5]

print(random.random())  # Print a random number from 0 - 1
print(random.randint(1, 6))  # Print a random integer from start - end
print(random.choice(myList))  # Print a Random choice in a list
random.shuffle(myList) # Shuffle the list

print(myList)

joke = pyjokes.get_joke('en', 'neutral')
print ( joke )
