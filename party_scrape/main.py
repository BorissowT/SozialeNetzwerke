import datetime
import json
import os
from datetime import time
from time import sleep

import sqlalchemy
import tweepy

from party_scrape.db_connect.db_settings import Tweet, session, Party

CONSUMER_KEY = os.getenv('twitter_consumer_key')
SECRET_KEY = os.getenv('twitter_consumer_secret')
ACCESS_TOKEN = os.getenv('twitter_access_token')
ACCESS_TOKEN_SECRET = os.getenv('twitter_access_token_secret')

auth = tweepy.OAuthHandler(CONSUMER_KEY, SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

amount_of_tweets_pro_call = 10000
until_date = "2022-06-07"
total_tweets = 100000

cdu_obj = session.query(Party).filter(Party.title == "CDU").first()
spd_obj = session.query(Party).filter(Party.title == "SPD").first()
gruenen_obj = session.query(Party).filter(Party.title == "GRÜNEN").first()
fdp_obj = session.query(Party).filter(Party.title == "FDP").first()
linke_obj = session.query(Party).filter(Party.title == "LINKE").first()
afd_obj = session.query(Party).filter(Party.title == "AFD").first()
parties_obj_list = [cdu_obj, spd_obj, gruenen_obj, fdp_obj, linke_obj, afd_obj]


def add_tweets_to_db(elem):
    mentioned_parties = scan_tweet_text_for_parties(elem.full_text)
    mentioned_parties_objects = [party for party in parties_obj_list if party.title in mentioned_parties]
    if len(mentioned_parties) > 0:
        tweet = Tweet()
        tweet.id = elem.id
        tweet.amount_of_likes = int(elem._json["favorite_count"])
        tweet.amount_of_retweets = elem.retweet_count
        tweet.date_created = elem.created_at
        tweet.text = elem.full_text
        for party_elem in mentioned_parties_objects:
            tweet.parties.append(party_elem)
        session.add(tweet)
        session.commit()


def scan_tweet_text_for_parties(text: str):
    parties_in_text = []
    CDU = {"title": "CDU", "titles": ["CDU", "Cdu", "cdu"]}
    FDP = {"title": "FDP", "titles": ["FDP", "Fdp", "fdp"]}
    LINKE = {"title": "LINKE", "titles": ["LINKE", "Linke", "linke"]}
    SPD = {"title": "SPD", "titles": ["SPD", "Spd", "spd"]}
    GRUNEN = {"title": "GRÜNEN", "titles": ["gruenen", "Gruenen", "GRUENEN", "grünen", "Grünen", "GRÜNEN", "Gruene"]}
    AFD = {"title": "AFD", "titles": ["AFD", "Afd", "afd", "AfD"]}
    parties = [CDU, FDP, LINKE, SPD, GRUNEN, AFD]
    for party in parties:
        for title in party["titles"]:
            if title in text:
                parties_in_text.append(party["title"])

    return parties_in_text


def do_query():
    cursor = tweepy.Cursor(api.search_tweets,
                           lang="de",
                           q='CDU OR SPD OR FDP OR LINKE OR GRÜNEN OR AFD',
                           tweet_mode="extended",
                           #until=until_date,
                           ).items(amount_of_tweets_pro_call)
    for elem in cursor:
        try:
            add_tweets_to_db(elem)
        except sqlalchemy.exc.IntegrityError:
            print("the same tweet. do rollback: ", datetime.datetime.now())
            session.rollback()


def do_query_once_15min():
    call_iterator_counter = 0
    while call_iterator_counter < (total_tweets/amount_of_tweets_pro_call):
        call_iterator_counter += 1
        try:
            do_query()
        except tweepy.errors.TooManyRequests:
            print("too many requests. wait 15 minutes ", datetime.datetime.now())
            sleep(60 * 15)
    session.close()


do_query_once_15min()




