# Twitter-Sentiment-on-Cryptocurrencies

## Overview
The recent price breakout of Bitcoin and alternatives has generated an increasing amount of hype and speculation around these brand new assest classes. The price is mostly driven by the speculation on the future potential of these cryptocurrencies instead of their current utilities and adoption. Therefore, the cryptocurrency market movements are heavily affected by the sentiment of speculators invested in this space. Twitter and similar social platforms provide a large amount of data to help study the sentiment of investors in the early stage of cryptocurrency devolopment. 

This is analysis, I use Twitter to learn more about the sentiment regarding the top 10 most popular cryptocurrencies (as of Feb,2018) and rank the polarity in descending order.

## Dependencies
The [demo code](https://github.com/llSourcell/twitter_sentiment_challenge/blob/master/demo.py) uses the tweepy library to access the Twitter API and the TextBlob library to perform Sentiment Analysis on each Tweet. My data analysis extension includes Numpy, Pandas library for storing and displaying result data, Matplotlib for data visualizaiton.
* tweepy (http://www.tweepy.org/)
* textblob (https://textblob.readthedocs.io/en/dev/)

## Usage
Once you have your dependencies installed via pip, run the script in terminal via

```
python demo.py
```

## Credit
This is the follow up code from the Twitter Sentiment Analyzer challenge for 'Learn Python for Data Science #2' by @Sirajology: [Siraj Raval](https://github.com/llSourcell). 
