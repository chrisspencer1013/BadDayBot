import tweepy
from textblob import TextBlob
import random
import datetime as dt

from keys import *
from links import *

tweets_this_session = 0
#currentTime = strftime("%Y-%m-%d %H:%M:%S",gmtime())
print("BAD DAY BOT! LET'S MAKE SOMEONES DAY A LITTLE BETTER!")#or at least post a picture to twitter lul
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
except:
    print("Error: Authentication Failure")
    
user = api.me()

for follower in tweepy.Cursor(api.followers).items():
    follower.follow() #follow everyone that is following the bot
    
#TODO: unfriend peeps on the blacklist

friend_list = []
print("Current allowed users:")
for friend in user.friends():
    print(friend.screen_name)
    friend_list.append(friend.id_str)
    
#print(friend_list)

class TweetListener(tweepy.StreamListener):
    def on_status(self, status):
        if "RT " not in status.text:
            print("\n"+status.text)
            results = TextBlob(status.text)
            print("\t"+str(results.sentiment.polarity))
            if (results.sentiment.polarity < -0.5):
                image_link = CuteAnimalLink()
                text_out = "@"+status.user.screen_name+" Bad day? Here's a cute animal! "+ image_link
                print(text_out)
                api.update_status(text_out,status.id_str)
                tweets_this_session+=1
            print("____________\n")
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False


tweetListenerInstance = TweetListener()
tweetStream = tweepy.Stream(auth = api.auth, listener=TweetListener())
tweetStream.filter(follow=friend_list)









