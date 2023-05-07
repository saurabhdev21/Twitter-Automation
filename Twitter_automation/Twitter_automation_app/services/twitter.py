import tweepy


def get_tweet_text(tweet_link):
    # Authenticate with Twitter
    consumer_key = 'dU9FZTZTbGVHclU4RE94Y0RZWnU6MTpjaQ'
    consumer_secret = 'dpULsN1NyHWtb7VBUm8yeqDDbfNocXNaaVEk09pV04TTdwVEZm'
    access_token = '899947006302408704-MYxhwWKjigRN88qaaQjr6C17pmhpDCN'
    access_token_secret = 'yZbe2kJl5Az0oShOM5ZHAmL0SyzI1CVLCEKMpAFfP3xqU'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create the API object
    api = tweepy.API(auth)

    # Get the tweet text using the Twitter API
    tweet_id = get_tweet_id(tweet_link)
    tweet = api.get_status(tweet_id, tweet_mode='extended')
    # return "sa"
    return tweet.full_text


def get_tweet_id(tweet_link):
    return tweet_link.split('/')[-1]
