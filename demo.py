# dependencies: 
import nltk
from textblob import TextBlob
import tweepy
import matplotlib.pylab as plt
import pandas as pd
import numpy as np
import operator
from datetime import datetime, timedelta

# retrive keys and tokens from twitter api
consumer_key = "UvUeLy0XaLSk9EmR1LdaqZXWR"
consumer_secret = "WM5ChOtqXOWLoPXcnsWEX0RCR20wEGl8Y92wfmfDcpOVfiyELr"
access_token = "328461368-zS0oD8e2wAInPxagoTcQhTAwm9FLuTJxzicpDRhu"
access_tokent_secret = "CDKYVGpayUBNkkL0KNwp96ipUgRpaWWljvYkTGBaVHCZj"

# use tweepy to handle api tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_tokent_secret)
api = tweepy.API(auth)

# Prepare the parameters:
# List of top 10 crytocurrencies as of Feb, 2018:
coin_names = ['Bitcoin', 'Ethereum', 'Ripple', 'Bitcoin Cash', 
              'Cardano', 'Litecoin', 'Stellar', 'NEO','EOS', 'IOTA']
# hashtag related to the coin
hashtag = "cryptocurrency"
# time interval is set to 30 most recent days:
since_date = (datetime.now() - timedelta(days=30)).strftime ("%Y-%m-%d")
until_date = datetime.now().strftime ("%Y-%m-%d")

# retrieve tweets and store in a dictionary:
all_polarities = dict()
for coin in coin_names:
    this_coin_polarities = []
    this_coin_tweets = api.search(q= [hashtag, coin], count = 100, since = since_date, until = until_date)
    for tweet in this_coin_tweets:
        analysis = TextBlob(tweet.text)
        #Get the label corresponding to the sentiment analysis
        this_coin_polarities.append(analysis.sentiment[0])
    #Save the mean for final results
    all_polarities[coin] = np.mean(this_coin_polarities)

# create a function that concludes the polarity of analysis:
def get_polarity(x, neutral = 0):
    if x > neutral:
        return "Positive"
    elif x == 0:
        return "Neutral"
    else:
        return "Negative"

# summarize the result using pandas dataframe:
summary = pd.DataFrame(list(all_polarities.items()), columns=['Crypto Currency', 'Polarity'])
summary['Sentiment'] = summary.Polarity.apply(get_polarity)
summary

# sort the dictionary based on values using operator
all_polarities = dict(sorted(all_polarities.items(), key=operator.itemgetter(1),reverse=True))

# visualize the data
plt.figure(figsize=(11,7))
plt.bar(range(len(all_polarities)), list(all_polarities.values()), align = 'center')
plt.xticks(range(len(all_polarities)), list(all_polarities.keys()))
plt.xlabel("Crypto Currency")
plt.ylabel("Sentiment Polarity")
plt.show()

