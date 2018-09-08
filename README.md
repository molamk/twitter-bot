# How to build a Twitter bot?

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

## Table of Contents

- [Prerequisites](#prerequisites)
- [Environment setup](#environment-setup)
- [Authenticate your app](#authenticate-your-app)
- [Create a Tweet listener](#create-a-tweet-listener)
- [Fire up the stream!](#fire-up-the-stream)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Prerequisites

```bash
# Create a Twitter app and grab your credenials

# Install dependencies
pip3 install git+https://github.com/tweepy/tweepy
pip3 install python-dotenv
```

## Environment setup

```bash
# Create an .env file, it should look like this
TWITTER_CONSUMER_KEY=<your_consumer_key>
TWITTER_CONSUMER_SECRET=<your_consumer_secret>
TWITTER_ACCESS_TOKEN=<your_access_token>
TWITTER_ACCESS_TOKEN_SECRET=<your_access_token_secret>
```

## Authenticate your app

```python
import os
import dotenv
import tweepy

# Load the environment variables
dotenv.load_dotenv()

auth = tweepy.OAuthHandler(
    os.getenv("TWITTER_CONSUMER_KEY"),
    os.getenv("TWITTER_CONSUMER_SECRET"))

auth.set_access_token(
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
```

## Create a Tweet listener

```python
import tweepy

class TweetListener(tweepy.StreamListener):
    def on_data(self, data):
        # Print the Tweet
        print(data)
        print(100 * '*')
        return True

    def on_error(self, status):
        print(status)
```

## Fire up the stream!

```python
# Keywords example
keywords = ['bitcoin', 'ethereum', 'ripple']

listener = TweetListener()
stream = tweepy.Stream(auth, listener, tweet_mode='extended')
stream.filter(track=keywords)
```
