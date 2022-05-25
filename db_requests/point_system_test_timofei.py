from db_connect.db_settings import Tweet, session

data = session.query(Tweet).filter()


