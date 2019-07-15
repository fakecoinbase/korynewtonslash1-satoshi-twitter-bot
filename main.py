import tweepy as tp
import time

from settings import *
from streaming import MyStreamListener
from scheduled_tweet import ScheduledTweet
from data import Retrieve_Data


# twitter credentials
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_secret = ACCESS_SECRET
fixer_key = FIXER_KEY


if __name__ == "__main__":
    # Get data, store in price_data.txt
    Retrieve_Data()

    # Initialize stream to listen for mentions
    myStreamListener = MyStreamListener()
    myStream = tp.Stream(auth=myStreamListener.api.auth,
                         listener=myStreamListener)
    myStream.filter(track=['1satoshibot'], is_async=True)

    while True:
        ScheduledTweet()
        wait = 30 * 60
        time.sleep(wait)
        print(f'waited {wait} seconds')
