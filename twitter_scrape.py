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

amount_of_tweets = 100


def add_cursor_to_db(cursor, party):
    for i in cursor:
        tweet = Tweet()
        tweet.amount_of_retweets = i.retweet_count
        tweet.amount_of_likes = i.favorite_count
        tweet.text = i.full_text
        tweet.party = party
        session.add(tweet)
        session.commit()


cdu_cursor = tweepy.Cursor(api.search_tweets, q="CDU", tweet_mode="extended").items(amount_of_tweets)
add_cursor_to_db(cdu_cursor, party="CDU")

spd_cursor = tweepy.Cursor(api.search_tweets, q="SPD", tweet_mode="extended").items(amount_of_tweets)
add_cursor_to_db(spd_cursor, party="SPD")

gruene_cursor = tweepy.Cursor(api.search_tweets, q="GRÜNE", tweet_mode="extended").items(amount_of_tweets)
add_cursor_to_db(gruene_cursor, party="GRÜNE")

fpd_cursor = tweepy.Cursor(api.search_tweets, q="FPD", tweet_mode="extended").items(amount_of_tweets)
add_cursor_to_db(fpd_cursor, party="FPD")

linke_cursor = tweepy.Cursor(api.search_tweets, q="LINKE", tweet_mode="extended").items(amount_of_tweets)
add_cursor_to_db(linke_cursor, party="LINKE")

afd_cursor = tweepy.Cursor(api.search_tweets, q="AFD", tweet_mode="extended").items(amount_of_tweets)
add_cursor_to_db(afd_cursor, party="AFD")

session.close()


