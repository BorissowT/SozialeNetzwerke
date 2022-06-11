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


def do_query():
    cursor = tweepy.Cursor(api.search_tweets,
                           lang="de",
                           q='CDU OR SPD OR FDP OR LINKE OR GRÜNEN OR AFD',
                           tweet_mode="extended",
                           # until=until_date,
                           ).items(1)
    return cursor


try:
    elem = do_query().next()
    tweet = Tweet()
    tweet.id = elem.id
    tweet.date_created = elem.created_at
    tweet.amount_of_retweets = elem.retweet_count
    tweet.amount_of_likes = int(elem._json["favorite_count"])
    tweet.text = "first schema test"
    session.add(tweet)
    party = session.query(Party).first()
    party.tweets.append(tweet)
    session.commit()
except sqlalchemy.exc.IntegrityError:
    print("same tweet")

session.close()

