#!/usr/bin/env python
# coding: utf-8

# In[20]:


import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
def process_tweets(tweet):
    tweet = re.sub(r'\$\w*', '', tweet)
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    tweet = re.sub(r'https?://[^\s\n\r]+','',tweet)
    tweet = re.sub(r'#','', tweet)

    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)
    
    stopwords_english = stopwords.words('english')
    punctuations = string.punctuation
    
    stemmer = PorterStemmer()
    processed_tweet = []
    for token in tweet_tokens:
        if(token not in stopwords_english and token not in punctuations):
            processed_tweet.append(stemmer.stem(token))
    return processed_tweet


# In[21]:


from nltk.corpus import twitter_samples
def generate_tweets():
    nltk.download('twitter_samples')
    all_positive_tweets = twitter_samples.strings('positive_tweets.json')
    all_negative_tweets = twitter_samples.strings('negative_tweets.json')
    return all_positive_tweets, all_negative_tweets

