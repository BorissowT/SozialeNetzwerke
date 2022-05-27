import tweepy
from pprint import pprint

# from db_connect.db_settings import Tweet

def load_creds(path):
    credentials_dict = {}
    content = open(path, "r").readlines()
    for line in content:
        key, value = line.strip().split("=")
        credentials_dict[key] = value
    return credentials_dict

def prep_api(credentials:dict):
    auth = tweepy.OAuthHandler(credentials["consumer_key"], credentials["consumer_secret"])
    auth.set_access_token(credentials["access_token"], credentials["access_token_secret"])
    api = tweepy.API(auth)
    return api

def which_party(to_check:str, parties:list=["CDU","SPD","AFD","GRÜNE","FDP","LINKE"]):
    for party in parties:
        if(party in to_check or party.lower() in to_check):
            return party


def get_tweets(api, amount_of_tweets=10):
    return_list_of_dict = []
    test_cursor = tweepy.Cursor(api.search_tweets, q="CDU OR SPD OR AFD OR GRÜNE OR FDP OR LINKE", lang="de", tweet_mode="extended").items(amount_of_tweets)
    for tweet in test_cursor:
        party = which_party(tweet.full_text)
        single_tweet = {
            "full_text"     : tweet.full_text,
            "favorite_count": tweet.favorite_count,
            "retweet_count" : tweet.retweet_count,
            "party"         : party
        }
        pprint(single_tweet)
        # pprint(tweet.full_text)
        # pprint(tweet.favorite_count)
        # pprint(tweet.retweet_count)

    # for i in cursor:
    #     tweet = Tweet()
    #     tweet.amount_of_retweets = i.retweet_count
    #     tweet.amount_of_likes = i.favorite_count
    #     tweet.text = i.full_text
    #     tweet.party = party
    #     session.add(tweet)
    #     session.commit()



def main():
    search_parties = ["CDU","SPD","AFD","GRÜNE","FDP","LINKE"]
    creds_path = "/home/cantuerk/data_science_project/SozialeNetzwerke/creds.txt"
    credentials:dict=load_creds(creds_path)
    api = prep_api(credentials)
    cursor = get_tweets(api)
    ret = which_party(search_parties, "Hallo ich bin von der FDP")
    # read_cursor(cursor)

if __name__=="__main__":
    main()