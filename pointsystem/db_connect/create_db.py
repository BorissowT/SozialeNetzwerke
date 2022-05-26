from sqlalchemy_utils import database_exists
from pointsystem.db_connect.db_settings import engine, Tweet, session, Base

if not database_exists(engine.url):
    Base.metadata.create_all(bind=engine)

tweet = Tweet()
tweet.amount_of_retweets = 12
tweet.amount_of_likes = 1
tweet.text = "first schema test"
tweet.party = "testparty"
session.add(tweet)
session.commit()
session.close()
