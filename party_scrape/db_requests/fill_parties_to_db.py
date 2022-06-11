from party_scrape.db_connect.db_settings import Party, session

parties = {"CDU", "SPD", "GRÜNEN", "FDP", "LINKE", "AFD"}


def fill_parties():
    for title in parties:
        party = Party()
        party.title = title
        party.amount_of_references = 0
        session.add(party)
        session.commit()
        session.close()


fill_parties()