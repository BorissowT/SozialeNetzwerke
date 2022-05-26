import os
import tweepy
from db_settings_party_scrape import Tweet, session


CONSUMER_KEY = os.getenv('twitter_consumer_key')
SECRET_KEY = os.getenv('twitter_consumer_secret')
ACCESS_TOKEN = os.getenv('twitter_access_token')
ACCESS_TOKEN_SECRET = os.getenv('twitter_access_token_secret')

auth = tweepy.OAuthHandler(CONSUMER_KEY, SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

amount_of_tweets = 900


def add_cursor_to_db(cursor):
    for i in cursor:
        tweet = Tweet()
        tweet.amount_of_retweets = i.retweet_count
        tweet.amount_of_likes = i.favorite_count
        tweet.text = i.full_text
        session.add(tweet)
        session.commit()


cursor = tweepy.Cursor(api.search_tweets, lang="de", q='CDU OR SPD OR FDP OR LINKE OR GRÜNEN OR AFD', tweet_mode="extended").items(amount_of_tweets)
add_cursor_to_db(cursor)

session.close()


