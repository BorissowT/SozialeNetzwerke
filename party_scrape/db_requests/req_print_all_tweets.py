from party_scrape.db_connect.db_settings import Tweet, session

tweets = session.query(Tweet).all()
for tweet in tweets:
    print(tweet.id)
    print(tweet.text)
    for party in tweet.parties:
        print(party.title)
    print("----")
session.close()
