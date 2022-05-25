from db_connect.db_settings import Tweet, session


def get_party_points(party) -> int:
    tweets = session.query(Tweet).filter(Tweet.party == party).all()
    points = 0
    for tweet in tweets:
        points += tweet.amount_of_likes
        points += tweet.amount_of_retweets*2
    return points


cdu_points = get_party_points("CDU")
spd_points = get_party_points("SPD")
grunen_points = get_party_points("GRÜNEN")
fpd_points = get_party_points("FPD")
linke_points = get_party_points("LINKE")
afd_points = get_party_points("AFD")

parties_list = [cdu_points, spd_points, grunen_points, fpd_points, linke_points, afd_points]
total_points = sum(parties_list)


print("CDU: {}%".format(format(cdu_points/total_points*100, ".2f")))
print("SPD: {}%".format(format(spd_points/total_points*100, ".2f")))
print("GRÜNEN: {}%".format(format(grunen_points/total_points*100, ".2f")))
print("FPD: {}%".format(format(fpd_points/total_points*100, ".2f")))
print("LINKE: {}%".format(format(linke_points/total_points*100, ".2f")))
print("AFD: {}%".format(format(afd_points/total_points*100, ".2f")))
