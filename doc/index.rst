======================================================================
twitter-sentiment: Twitter library to explore sentiments behind tweets
======================================================================

*Release v0.0.1*

twitter-sentiment is a light-weight Python 3 library that allows you to evaluate the sentiment of tweets. Behind the scene, twitter-sentiment classify tweets as either positive (1) or negative (0) and returns a ratio of positive tweets.

The library also includes features to get structured tweets, users, and user mentions to build and develop insights regarding users and their tweets.

::

    import twitterSentiment

    connection = twitterSentiment.API()
    search = connection.querySearch("Los Angeles", count=1, result_type='recent', lang='en')
    data = twitterSentiment.StructureStatusesData(search)
    sentiment = twitterSentiment.SentimentScore(data.getTweet())
    print(sentiment.getSentimentClassification())

    >> 0.6666

Features
--------
* Connect to the Twitter API in a matter of seconds
* Get ratio of positive tweets amongst the ones analyzed (ranges from 0 to 1)
* Get raw tweet response
* Get structured tweets, users, and user mentions data to leverage insights

Install it now
--------------
::

    pip install twitter-sentiment

Table of Contents
----------------
.. toctree::
    :maxdepth: 2

    license
    installation
    gettingstarted
    APIreference