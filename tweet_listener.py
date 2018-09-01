import tweepy

from tweet_status import TweetStatus


class TweetListener(tweepy.StreamListener):
    def on_data(self, data):
        print(TweetStatus(data))
        print(100 * '*')
        return True

    def on_error(self, status):
        print(status)
