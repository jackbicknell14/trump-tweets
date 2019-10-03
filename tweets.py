# General:
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing

# For plotting and visualization:
#from IPython.display import display
#import matplotlib.pyplot as plt
#import seaborn as sns
#%matplotlib inline

# Twitter App access keys for @user

# Consume:
CONSUMER_KEY = 'Woqu8EuBh9ICDXamssFKGpGG4'
CONSUMER_SECRET = 'xzGeNNce3pVtMteWJoRhiv81ftapoST1fRir9sDrcrcnLjZAIu'

# Access:
ACCESS_TOKEN  = '721227717975412736-vXZPTQOYZ8hzyeuj7PHYzozOdd95ddE'
ACCESS_SECRET = 'PK45GFbXw1YujfSGY6rNKpxEJD5rMwZtU7V4sPkLaZrfN'

# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv



def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print(f"...{len(alltweets)} tweets downloaded so far")

    #transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    #write the csv
    df = pd.DataFrame(outtweets)
    print(len(outtweets))

    df.to_csv('tweets.csv')



if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("realDonaldTrump")
