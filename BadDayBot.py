import tweepy
from textblob import TextBlob
import random
import datetime as dt

from keys import *

#currentTime = strftime("%Y-%m-%d %H:%M:%S",gmtime())
print("BAD DAY BOT! LET'S MAKE SOMEONE'S DAY A LITTLE BETTER!\n")#or at least post a picture to twitter lul
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
except:
    print("Error: Authentication Failure")
    
user = api.me()

for follower in tweepy.Cursor(api.followers).items():
    follower.follow() #follow everyone that is following the bot

#not yet tested cause I'm lazy
with open('blacklist.txt') as b: 
    blacklist = b.readlines()
    for user_id in blacklist:
        user.destroy_friendship(user_id)

friend_list = []
print("Currently followed users:")
for friend in user.friends():
    print("\t"+friend.screen_name)
    friend_list.append(friend.id_str)
    
#print(friend_list)

class TweetListener(tweepy.StreamListener):
    def on_status(self, status):
        if "RT " not in status.text:
            print("\n"+status.text)
            results = TextBlob(status.text)
            print("\t"+str(results.sentiment.polarity))
            if (results.sentiment.polarity < -0.5):
                text_out = createMessage(status.user.screen_name)
                print(text_out)
                api.update_status(text_out,status.id_str)
            print("____________\n")
    def on_error(self, status_code):
        if status_code == 420:
            return False

def createMessage(screen_name):
    with open('messages.txt') as f:
        message_templates = f.readlines()
    with open('links.txt') as f:
        links = f.readlines()
    return("@"+screen_name+" "+random.choice(message_templates)+" "+ random.choice(links))

print("\nLet's go!")
tweetListenerInstance = TweetListener()
tweetStream = tweepy.Stream(auth = api.auth, listener=TweetListener())
tweetStream.filter(follow=friend_list)









