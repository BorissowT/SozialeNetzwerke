# SozialeNetzwerke
aka Data science

## Install dependencies
1.Run `pip install poetry`

2.Run `poetry install` in root of project

3.Run `poetry shell` to access all dependencies in virtual environment

## Database Model
```
class Single_Tweet_Model(BASE):
    __tablename__ = 'tweets'
    id = Column('tweet_id', Integer, primary_key=True)
    party = Column(String(10))
    amount_of_retweets = Column('amount_of_retweets', Integer)
    amount_of_likes = Column('amount_of_likes', Integer)
    text = Column(String(500))
```
## Sample SQL Query
To use the query_db.py script you HAVE TO be in the SozialeNetwerke directory.
```
python3 query_db.py -q "SELECT tweet_id, text, party FROM tweets" -n 10
```