from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

connection = "sqlite:///twitter.db"
engine = create_engine(connection)

Base = declarative_base(name='Model')


class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column('tweet_id', Integer, primary_key=True)
    amount_of_retweets = Column('amount_of_retweets', Integer)
    amount_of_likes = Column('amount_of_likes', Integer)
    text = Column(String(500))


# Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
tweet = Tweet()
tweet.id = 1
tweet.amount_of_retweets = 100
tweet.amount_of_likes = 101
tweet.text = "test_text"

#session.add(tweet)
#session.commit()
tweets = session.query(Tweet).all()
for elem in tweets:
    print(elem.text)
session.close()