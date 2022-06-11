from party_scrape.db_connect.db_settings import Party, session

parties = session.query(Party).all()
for elem in parties:
    print(elem.title, ": ", len(elem.tweets))
session.close()