from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
# import os
#
# current_directory = os.getcwd()
# connection = "sqlite:///"+os.path.abspath('twitter.db')
connection = "sqlite:////home/tim/PycharmProjects/SozialeNetzwerke/db_connect/twitter.db"
engine = create_engine(connection)
Base = declarative_base(name='Model')


# TODO replies
class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column('tweet_id', Integer, primary_key=True)
    amount_of_retweets = Column('amount_of_retweets', Integer)
    amount_of_likes = Column('amount_of_likes', Integer)
    text = Column(String(500))


Session = sessionmaker(bind=engine)
session = Session()



