import tweepy
from keys import *
#stupid twitter bot that converts Times of India (ToI) tweets to Pig Latin for no reason whatsoever

def get_twt():
	pass

def pig_it():
	pass

def capital_format():
	pass
def post_twt():
	pass
def is_link():
	pass


auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

target = 'TimesOfIndia'

user = api.get_user(target)

number_of_tweets=200
tweets = api.user_timeline(screen_name='TimesOfIndia') 

print(type(tweets))


t = 'Tweeting in T-0 seconds'
api.update_status(t)