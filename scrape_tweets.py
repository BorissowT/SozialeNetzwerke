import tweepy
from sqlalchemy import select
import re
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

CONNECTION = "sqlite:////home/cantuerk/data_science_project/SozialeNetzwerke/all_tweets.db"
ENGINE = create_engine(CONNECTION)
BASE = declarative_base(name='Model')

class Single_Tweet_Model(BASE):
    __tablename__ = 'tweets'
    id = Column('tweet_id', Integer, primary_key=True)
    party = Column(String(10))
    amount_of_retweets = Column('amount_of_retweets', Integer)
    amount_of_likes = Column('amount_of_likes', Integer)
    text = Column(String(500))

def prepare_engine():
    connection = "sqlite:////home/cantuerk/data_science_project/SozialeNetzwerke/all_tweets.db"
    return create_engine(connection)

def prepare_session():
    session_maker = sessionmaker(bind=ENGINE)
    return session_maker()

def load_creds(path):
    credentials_dict = {}
    content = open(path, "r").readlines()
    for line in content:
        key, value = line.strip().split("=")
        credentials_dict[key] = value
    return credentials_dict

def prep_api(credentials:dict):
    auth = tweepy.OAuthHandler(credentials["consumer_key"], credentials["consumer_secret"])
    auth.set_access_token(credentials["access_token"], credentials["access_token_secret"])
    api = tweepy.API(auth)
    return api

def which_party(to_check:str, parties:list=["CDU","SPD","AFD","GRÜNE","FDP","LINKE"]):
    for party in parties:
        if(re.search(party, to_check, re.IGNORECASE)):
            return party
        
def get_tweets_n_add_to_db(api, session, amount_of_tweets):
    test_cursor = tweepy.Cursor(api.search_tweets, q="(CDU OR SPD OR AFD OR GRÜNE OR FDP OR LINKE)", lang="de", tweet_mode="extended").items(amount_of_tweets)
    for tweet in test_cursor:
        party = which_party(tweet.full_text)
        # Check if Tweet with this Tweet ID already exists in DB
        stmt = select(Single_Tweet_Model).where(Single_Tweet_Model.id == tweet.id)
        res = session.execute(stmt)
        if(not(res.scalars().all() == [])):
            continue # If it does skip this tweet
        
        if(party is None):
            continue
        db_tweet = Single_Tweet_Model()
        db_tweet.id = tweet.id
        db_tweet.amount_of_likes = tweet.favorite_count
        db_tweet.amount_of_retweets = tweet.retweet_count
        db_tweet.party = party
        db_tweet.text = tweet.full_text
        session.add(db_tweet)
    session.commit()
    session.close()

def get_db_length(session):
    tweets = session.query(Single_Tweet_Model).all()
    print(len(tweets))
    session.close()

def get_all_data(session):
    tweets = session.query(Single_Tweet_Model).all()
    for elem in tweets:
        print(elem.id, elem.party)
    session.close()

def main():
    creds_path = "/home/cantuerk/data_science_project/SozialeNetzwerke/creds.txt"
    credentials:dict=load_creds(creds_path)
    api = prep_api(credentials)
    session = prepare_session()
    get_all_data(session)
    get_tweets_n_add_to_db(api, session, 500)
    get_db_length(session)

if __name__=="__main__":
    main()