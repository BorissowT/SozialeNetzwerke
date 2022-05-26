from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

connection = "sqlite:////home/tim/PycharmProjects/SozialeNetzwerke/party_scrape/party_scrape.db"
engine = create_engine(connection)
Base = declarative_base(name='Model')


class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column('tweet_id', Integer, primary_key=True)
    amount_of_retweets = Column('amount_of_retweets', Integer)
    amount_of_likes = Column('amount_of_likes', Integer)
    text = Column(String(500))


Session = sessionmaker(bind=engine)
session = Session()



