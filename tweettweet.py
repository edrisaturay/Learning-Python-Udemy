# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 03:21:36 2020

@author: edris
"""

import tweepy
import time

consumer_key = 'nbSWPMv58BxEhTKuhcgVq2TCD'
consumer_secret = 'T8qfJ04hwoRYCKS488al3arzQbFYqIYR7HONtTktPDjxCnUktw'
access_token = '728119313605918721-gnEQD3hpH5DiYhJAxFGiBKrItZzXq2D'
access_token_secret = 'jF0Dh6FRSDDFFVoe4oCqd1KdXPLenNs7nKLV0HAtyb2gm'

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    except : 
        print('You\'ve reached the end')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

'''
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

user = api.me()

print ( user.name )
print ( user.screen_name)
print ( user.followers_count )

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.screen_name == '08e0v74wOYjQxOS': 
        follower.follow()
    print(follower.screen_name)
'''
    
searchString  = 'Edrisa'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, searchString).items(numbersOfTweets): 
    try: 
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e: 
        print ( e.reason )
    except StopIteration:
        break