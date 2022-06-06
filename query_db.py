from sqlalchemy import text
from scrape_tweets import prepare_session
import argparse

def cli() -> dict:
    """
    Returns a dict with the needed args.
    """
    parser = argparse.ArgumentParser()
    reqArgs = parser.add_argument_group("Required Arguments")
    reqArgs.add_argument("-q", "--query", help = "SQL Query", required=True)
    reqArgs.add_argument("-n", "--amount_tweets", help = "Amount of Tweets")
    args = parser.parse_args()
    return {
        "query"            : args.query,
        "amount_tweets"    : args.amount_tweets,
    }

def exec_query(query:str, amount_tweets:int = None):
    # Sample Query : "SELECT tweet_id, text, party FROM tweets"
    session = prepare_session()
    textual_sql = text(query)
    query_res = session.execute(textual_sql)
    if(amount_tweets == None):
        for tweet in query_res:
            print(tweet)
    else:
        for idx, tweet in enumerate(query_res):
            if(int(idx) == int(amount_tweets)):
                break
            print(tweet)

if __name__ == "__main__":
    args = cli()
    exec_query(args["query"], args["amount_tweets"])