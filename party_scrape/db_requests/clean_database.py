from party_scrape.db_settings_party_scrape import Tweet, session

if input("are you sure you want to clean database entirely? yes:Y ") == 'Y':
    print("YES")
    tweets = session.query(Tweet).delete()
    session.commit()
    print("DB Cleaned")
else:
    print("NO. Operation stopped")
