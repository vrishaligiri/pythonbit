import tweepy
from textblob import TextBlob

consumer_key = 'v10tEYcDYJb3yHAbEJsVqavKx'
consumer_secret = 'nDpDT4rj4djK5ybgHlVBgqjeIQzibxc5Ko2HfquonyJsiQlekH'


access_token = '961695824458731527-HWwhdIWpdnXTUT5ivYig3Vy0bGaIp4G'
access_token_secret = '7A9hR0vZAeqfSIq3Dpl20LKMQv02WAYi847LvYyZvDZQi'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')


for tweet in public_tweets:
	print(tweet.text.encode("utf-8"))
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)