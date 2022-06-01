import tweepy
from pprint import pprint


def load_creds(path):
    credentials_dict = {}
    content = open(path, "r").readlines()
    for line in content:
        key, value = line.strip().split("=")
        credentials_dict[key] = value
    return credentials_dict


def prep_api(credentials: dict):
    auth = tweepy.OAuthHandler(credentials["consumer_key"], credentials["consumer_secret"])
    auth.set_access_token(credentials["access_token"], credentials["access_token_secret"])
    api = tweepy.API(auth)
    return api


def which_party(to_check: str, parties: list = ["CDU", "SPD", "AFD", "GRÜNE", "FDP", "LINKE"]):
    for party in parties:
        if party in to_check or party.lower() in to_check or party.capitalize() in to_check:
            return party


def get_tweets(api, amount_of_tweets=10) -> list:
    list_of_tweets = []
    test_cursor = tweepy.Cursor(api.search_tweets, q="CDU OR SPD OR AFD OR GRÜNE OR FDP OR LINKE", lang="de",
                                tweet_mode="extended").items(amount_of_tweets)
    for tweet in test_cursor:
        party = which_party(tweet.full_text)
        single_tweet = {
            "full_text": tweet.full_text,
            "favorite_count": tweet.favorite_count,
            "retweet_count": tweet.retweet_count,
            "party": party
        }
        list_of_tweets.append(single_tweet)
    return list_of_tweets


def main():
    creds_path = "/home/cantuerk/data_science_project/SozialeNetzwerke/creds.txt"
    credentials: dict = load_creds(creds_path)
    api = prep_api(credentials)
    list_of_tweets = get_tweets(api)
    pprint(list_of_tweets)
    # TODO : Iterate through list of tweets, add all tweets where party != None to DB


if __name__ == "__main__" :
    main()
