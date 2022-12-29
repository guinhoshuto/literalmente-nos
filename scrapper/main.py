import pandas as pd
import snscrape.modules.twitter as twitter
import utils
from rich import print

username = 'Marcellus_V'
tweet_columns = ['Datetime', 'Id', 'Text', 'Username', 'Media', 'Url']
tweet_list = []

def is_mention(tweet):
    if tweet[0] == '@':
        return True
    return False

def quote_another_tweet(tweet):
    last_word = utils.get_last_word(tweet) 
    if last_word[0:12] == 'https://t.co/':
        return True
    return False 
    
def get_quoted_tweet(tweet):
    if quote_another_tweet(tweet.content):
        return twitter.TwitterTweetScraper()
    return ''

def has_media(tweet):
    if tweet.media is None:
        return False
    return True

for i, tweet in enumerate(twitter.TwitterSearchScraper('nós from:'+ username).get_items()):
    print(tweet)
    print(i, tweet.content)
    if i > 900:
        break
    tweet_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.media, tweet.url ])

df = pd.DataFrame(tweet_list, columns=tweet_columns)
df.to_csv('./tweets.csv')

