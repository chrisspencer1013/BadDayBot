import tweepy
from textblob import TextBlob
import random
import keys
import Links

tweetsThisSession = 0
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
except:
    print("Error: Authentication Failure")

user = api.me()
for friend in user.friends():
    print(friend.screen_name)

tweets = api.home_timeline()
for tweet in tweets:
    results = TextBlob(tweet.text)
    print("\n")
    print(tweet.text)
    print(results.sentiment.polarity)
    if (results.sentiment.polarity < -0.5 and tweetsThisSession < 3):
        imageLink = CuteAnimalLink()
        #api.update_status("Bad day? Here's a cute animal! "+ imageLink +" (if you are not having a bad day, please reply to this comment so I can fix the bot)",tweet.id_str)
        tweetsThisSession+=1
        print("TWEET OUT HERE!")

   




