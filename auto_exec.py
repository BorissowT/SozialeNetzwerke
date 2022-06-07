from scrape_tweets import main
import tweepy
import time

def auto_main():
    while(True):
        try:
            main()
        except tweepy.errors.TooManyRequests:
            print("EXCEPTION")
            pass
        time.sleep(17*60)
    
if __name__=="__main__":
    auto_main()
        
