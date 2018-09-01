#!/usr/local/bin/python3

import tweepy
import pprint
from tweet_status import TweetStatus

import dotenv
import os

dotenv.load_dotenv()


class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        pprint.pprint(TweetStatus(data))
        print(100 * '*')
        return True

    def on_error(self, status):
        print(status)


def main():
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(
        os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"))
    auth.set_access_token(
        os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))

    stream = tweepy.Stream(auth, listener, tweet_mode='extended')
    stream.filter(track=['trump'])


if __name__ == '__main__':
    main()
