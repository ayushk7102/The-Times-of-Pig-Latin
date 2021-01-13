import tweepy
from keys import *
import time
#stupid twitter bot that converts Times of India (ToI) tweets to Pig Latin for no reason whatsoever
STATUS_ID_LOG = 'last_seen_status_id.txt'



def get_twt():
	pass

def pig_it(tweet):
	words = tweet.split(' ')
	actual_words = ""

	for word in words:
		a_string = word
		matches = ["https", "@", "via", "RT"]

		if any(x in a_string for x in matches):
			pass
		else:
			actual_words += (word+ " ")
	
	final_str = ""

	consonants = "bcdfghjklmnpqrstvwxyz"

	actual_words = actual_words.strip()
	actual_words = actual_words.replace(':', '')
	actual_words = actual_words.replace('&amp', 'and')

	for word in actual_words.split(' '):
		
		if(word.isdigit()):
			final_str+=word+ " "
			continue

		last = ""
		i = 0
		for ch0 in word:
			ch = str(ch0).lower()


			if(ch in consonants):

				last+=str(ch)
				i+=1


			else:
				break

		pig_lat_word = word[i:]+last+"ay"

		pig_lat_word = pig_lat_word.capitalize()

		final_str+=pig_lat_word+ " "


	return final_str



	
def capital_format():
	pass
def post_twt():
	pass
def is_link():
	pass

def return_last_seen_id(STATUS_ID_LOG):
	f_read = open(STATUS_ID_LOG, 'r')
	last_seen_id = int(f_read.read().strip())
	f_read.close()
	return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return






auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)






def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = return_last_seen_id(STATUS_ID_LOG)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.

    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    target = 'TimesOfIndia'

    user = api.get_user(target)
    number_of_tweets=200
    last_id = ''


    tweets = api.user_timeline(screen_name='TimesOfIndia', since_ids='', tweet_mode='extended') 

    for tweet in reversed(tweets):
    	
    	#print(str(tweet.id)+' - ' + tweet.full_text, flush = True)
    	#print('\n')
    	pigged = pig_it(tweet.full_text)
    	print(pigged+ '\n')
    	last_seen_status_id = tweet.id
    	store_last_seen_id(last_seen_status_id, STATUS_ID_LOG)

    	try:
    		api.update_status(pigged)
    	except:
    		continue

   # for mention in reversed(mentions):
    #    print(str(mention.id) + ' - ' + mention.full_text, flush=True)
    #    last_seen_id = mention.id
     #   store_last_seen_id(last_seen_id, FILE_NAME)



        
while True:
    reply_to_tweets()
    time.sleep(15)

