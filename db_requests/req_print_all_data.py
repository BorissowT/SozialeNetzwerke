from db_connect.db_settings import Tweet, session

tweets = session.query(Tweet).all()
for elem in tweets:
    print(elem.text)
session.close()
