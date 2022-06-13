import os
import sqlite3

import sqlalchemy
import tweepy

from party_scrape.db_connect.db_settings import Party, Tweet, session, Base

CONSUMER_KEY = os.getenv('twitter_consumer_key')
SECRET_KEY = os.getenv('twitter_consumer_secret')
ACCESS_TOKEN = os.getenv('twitter_access_token')
ACCESS_TOKEN_SECRET = os.getenv('twitter_access_token_secret')

auth = tweepy.OAuthHandler(CONSUMER_KEY, SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

until_date = "2022-06-07"

def do_query():
    cursor = tweepy.Cursor(api.search_tweets,
                           lang="de",
                           q='CDU OR SPD OR FDP OR LINKE OR GRÜNEN OR AFD',
                           tweet_mode="extended",
                           until=until_date,
                           ).items(1)
    return cursor


data = do_query().next()
print(int(data._json["retweeted_status"]["favorite_count"]))
# id = 1533961925712875522
# status = api.get_status(id)
# print(status._json["retweeted_status"]["favorite_count"])

session.close()

