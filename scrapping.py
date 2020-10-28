

import datetime as dt
import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = '7jX7u5xWaYQMUMimAAqETiaAA'
consumer_secret = 'cycRYS1om6Zca7xcMxUViApiKtWDKq5MXnzDRZZ4LCnoNzcnTb'
access_token = '1320349976011010048-NVCMZPEEzKpohc0BNOa0sQdUfcNa27'
access_token_secret = 'AY50HnmMuEJ86zItFFCInMttR49yLr5OxZxreEC21hJ6G'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="bitcoins",count=100,
                           lang="en"
                           ,since="2019-01-01").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])







