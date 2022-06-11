from party_scrape.db_connect.db_settings import Tweet, session, Party, association_table

if input("are you sure you want to clean database entirely? yes:Y ") == 'Y':
    print("YES")
    session.query(Tweet).delete()
    session.query(Party).delete()
    session.query(association_table).delete()
    session.commit()
    print("DB Cleaned")
else:
    print("NO. Operation stopped")
