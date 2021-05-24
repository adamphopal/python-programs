#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from textblob import TextBlob 
import sys, tweepy
import matplotlib.pyplot as plt
import os

def percentange(part,whole):
    return 100* float(part)/float(whole)

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

searchTerm = input("Enter keyword/hashtag to search about:")
noOfSearchTerms = int(input("Enter number of tweet to analyze:"))

tweets = tweepy.Cursor(api.search, q = searchTerm,lang = "en" ).items(noOfSearchTerms)

positive = 0
negative = 0
neutral= 0
polarity = 0
total = 0

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    print(analysis.sentiment.polarity)
    total += 1
    if(analysis.sentiment.polarity == 0):
        neutral += 1
        print("neutral increased " + str(neutral))
        
    elif(analysis.sentiment.polarity < 0.00):
        negative += 1
        print("negative increased " + str(negative))
        
    elif(analysis.sentiment.polarity > 0.00):
        positive += 1   
        print("positive increased " + str(positive))
    
print("positive "+str(positive))
print("negative "+str(negative))
print("neutral "+str(neutral))

positive = percentange(positive , total)
negative = percentange(negative , total)
neutral = percentange(neutral , total)

positive = format(positive , '.2f' )
negative = format(negative , '.2f' )
neutral = format(neutral , '.2f' )

print("positive %"+str(positive))
print("negative %"+str(negative))
print("neutral %"+str(neutral))

print("How are people reacting on #" + searchTerm + "by analyzing " + str(noOfSearchTerms)+ ' Tweets.')

if(polarity == 0):
    print("neutral")    
elif(polarity > 0):
    print("positive")
elif(polarity < 0):
    print("negative")
    
labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
sizes = [positive,neutral, negative ]
colors = ['yellowgreen',  'gold','red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on #' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()
