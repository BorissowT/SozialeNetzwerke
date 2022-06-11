from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship

# import os
#
# current_directory = os.getcwd()
# connection = "sqlite:///"+os.path.abspath('twitter.db')
from sqlalchemy.testing.schema import Table

connection = r"sqlite:///C:\Users\tim\PycharmProjects\tweets\party_scrape/twitter.db"
#connection = r"sqlite:////home/tim/PycharmProjects/tweets/party_scrape/twitter.db"
engine = create_engine(connection)

Base = declarative_base(name='Model')

association_table = Table(
    "association",
    Base.metadata,
    Column("tweet_id", ForeignKey("tweets.tweet_id")),
    Column("party_id", ForeignKey("party.party_id")),
)


class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column('tweet_id', Integer, primary_key=True)
    amount_of_retweets = Column('amount_of_retweets', Integer)
    amount_of_likes = Column('amount_of_likes', Integer)
    text = Column(String(500))
    date_created = Column(DateTime)
    parties = relationship("Party", secondary=association_table, back_populates="tweets")


class Party(Base):
    __tablename__ = 'party'
    id = Column('party_id', Integer, primary_key=True)
    title = Column('title', String(10))
    tweets = relationship("Tweet", secondary=association_table, back_populates="parties")


Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


