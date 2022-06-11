from party_scrape.db_connect.db_settings import Party, Tweet, session, Base

tweet = Tweet()
tweet.amount_of_retweets = 12
tweet.amount_of_likes = 1
tweet.text = "first schema test"
session.add(tweet)
party = session.query(Party).first()
party.tweets.append(tweet)
session.commit()
session.close()

