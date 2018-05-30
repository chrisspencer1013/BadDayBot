import tweepy
from textblob import TextBlob
import random
import datetime as dt

from keys import *
from links import *

tweetsThisSession = 0
#currentTime = strftime("%Y-%m-%d %H:%M:%S",gmtime())
#todo bad day bot welcome splash
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
except:
    print("Error: Authentication Failure")

user = api.me()
while True:
    now = dt.datetime.now()-dt.timedelta(minutes=15)
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow() #follow everyone that is following the bot
    for friend in user.friends():
        print(friend.screen_name)
        tweets = api.user_timeline(friend.screen_name,count=10)
        for tweet in tweets:
            if now < tweet.created_at:
                print('\n\tSkipping old tweets')
                break
            with open('replied.txt') as replied:#needs some work
                for id_string in replied:
                    if id_string = tweet.id_str:
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

   




