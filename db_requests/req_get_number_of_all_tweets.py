from db_connect.db_settings import Tweet, session

tweets = session.query(Tweet).all()
print(len(tweets))
session.close()
