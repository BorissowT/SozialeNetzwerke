from itertools import count
from scrape_tweets import Single_Tweet_Model, prepare_db_session, prepare_connection

def get_party_points(party) -> int:
    session = prepare_db_session(prepare_connection())
    tweets = session.query(Single_Tweet_Model).filter(Single_Tweet_Model.party == party).all()
    counter = 0
    for _ in tweets:
        counter += 1
    return counter


cdu_points = get_party_points("CDU")
spd_points = get_party_points("SPD")
grunen_points = get_party_points("GRÜNE")
fpd_points = get_party_points("FDP")
linke_points = get_party_points("LINKE")
afd_points = get_party_points("AFD")

parties_list = [cdu_points, spd_points, grunen_points, fpd_points, linke_points, afd_points]
total_points = sum(parties_list)


print("CDU: {}%".format(format(cdu_points/total_points*100, ".2f")))
print("SPD: {}%".format(format(spd_points/total_points*100, ".2f")))
print("GRÜNE: {}%".format(format(grunen_points/total_points*100, ".2f")))
print("FDP: {}%".format(format(fpd_points/total_points*100, ".2f")))
print("LINKE: {}%".format(format(linke_points/total_points*100, ".2f")))
print("AFD: {}%".format(format(afd_points/total_points*100, ".2f")))
