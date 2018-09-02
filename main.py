#!/usr/local/bin/python3

import os

import dotenv
import tweepy

from tweet_listener import TweetListener
from tweet_status import TweetStatus

dotenv.load_dotenv()

keywords = ['bitcoin', 'ethereum', 'ripple']


def main():
    listener = TweetListener()
    auth = tweepy.OAuthHandler(
        os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"))
    auth.set_access_token(
        os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))

    stream = tweepy.Stream(auth, listener, tweet_mode='extended')
    stream.filter(track=keywords)


if __name__ == '__main__':
    main()
