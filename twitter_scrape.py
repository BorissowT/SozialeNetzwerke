import os
import tweepy
from db_connect.db_settings import Tweet, session

CONSUMER_KEY = os.getenv('twitter_consumer_key')
SECRET_KEY = os.getenv('twitter_consumer_secret')
ACCESS_TOKEN = os.getenv('twitter_access_token')
ACCESS_TOKEN_SECRET = os.getenv('twitter_access_token_secret')


auth = tweepy.OAuthHandler(CONSUMER_KEY, SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

cursor = tweepy.Cursor(api.search_tweets, q="CDU", tweet_mode="extended").items(100)

# for i in cursor:
#     tweet = Tweet()
#     try:
#         #tweet.id = i.id
#         tweet.amount_of_retweets = i.retweet_count
#         tweet.amount_of_likes = i.favorite_count
#         tweet.text = i.full_text
#         session.add(tweet)
#         session.commit()
#     except Exception as e:
#         print(e)
#         print("same tweet")
#
# session.close()

tweets = session.query(Tweet).all()
for elem in tweets:
    print(elem.text)
session.close()
