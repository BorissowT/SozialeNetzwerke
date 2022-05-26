from party_scrape.db_settings_party_scrape import Tweet, session

tweets = session.query(Tweet).all()
print(len(tweets))
session.close()
