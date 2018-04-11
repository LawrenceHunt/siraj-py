import tweepy
from textblob import TextBlob

consumer_key = 'waURFVcCAgcisiInGCUUH1yEX'
consumer_secret = '5Sz2Ig11npA1e8FPdPNhbh2BhSpIXw351bz6kRadPLI7dg3nBo'

access_token = 	'399393729-L0omRzMuEMjfoYsw5gMrb6KVwGFQ492tewGoqLgm'
access_token_secret = '6Yv2JhBMOOSzwUYR8xutChqBzqjMB6clwk0T1oajStALc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
