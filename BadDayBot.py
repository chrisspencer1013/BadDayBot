import tweepy
from textblob import TextBlob
import random
import datetime as dt

from keys import *
from links import *

tweetsThisSession = 0
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
            print("____________\n")
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False


tweetListenerInstance = TweetListener()
tweetStream = tweepy.Stream(auth = api.auth, listener=TweetListener())
tweetStream.filter(follow=friend_list)






'''
now = dt.datetime.now()-dt.timedelta(minutes=15)

for friend in user.friends():
    print(friend.screen_name)
    tweets = api.user_timeline(friend.screen_name,count=10)
    for tweet in tweets:
        if now < tweet.created_at:
            print('\n\tSkipping old tweets')
            break
        with open('replied.txt') as replied:#needs some work
            for id_string in replied:
                if id_string == tweet.id_str:
                    break
        if "RT " in tweet.text:
            print("\n\tSkipping RT")
            break 
        results = TextBlob(tweet.text)
        print("\n\t"+str(tweet.created_at))
        print("\t"+tweet.text)
        print("\t"+str(results.sentiment.polarity))
        if (results.sentiment.polarity < -0.5 and tweetsThisSession < 3):
            imageLink = CuteAnimalLink()
            #api.update_status("Bad day? Here's a cute animal! "+ imageLink +" (if you are not having a bad day, please reply to this comment so I can fix the bot)",tweet.id_str)
            tweetsThisSession+=1
            print("\t\tTWEET OUT HERE! " + CuteAnimalLink())
    print("____________\n")
    #time.sleep(10)
    break#for testing

   
'''



