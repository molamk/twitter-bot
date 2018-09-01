import json

from tweet_author import TweetAuthor
from tweet_utils import extract_keyword


class TweetStatus():
    def __init__(self, raw_data):
        data = json.loads(raw_data)
        self.created_at = data['created_at']
        self.tweet_id = data['id']

        self.hashtags = extract_keyword(
            data['entities']['hashtags'], 'text')
        self.mentions = extract_keyword(
            data['entities']['user_mentions'], 'screen_name')
        self.urls = extract_keyword(
            data['entities']['urls'], 'expanded_url')

        try:
            self.text = data['extended_tweet']["full_text"]

            et = data['extended_tweet']['entities']
            self.hashtags.extend(extract_keyword(et['hashtags'], 'text'))
            self.mentions.extend(extract_keyword(
                et['user_mentions'], 'screen_name'))
            self.urls.extend(extract_keyword(et['urls'], 'expanded_url'))
        except KeyError:
            self.text = data['text']

        self.retweet_count = data['retweet_count']
        self.favorite_count = data['favorite_count']
        self.lang = data['lang']
        self.author = TweetAuthor(data['user'])

        if 'retweeted_status' in data:
            self.retweeted_status = TweetStatus(
                json.dumps(data['retweeted_status']))

    def __repr__(self):
        from pprint import pformat
        return pformat(vars(self), indent=4)
