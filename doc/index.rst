======================================================================
twitter-sentiment: Twitter library to explore sentiments behind tweets
======================================================================

*Release v0.1.0*

twitter-sentiment is a lightway python 3 library that allows you to evaluate the sentiment of tweets.  
The library also includes features to get structured tweets, users, and user mentions to build and develop insight regarding users and their tweets.

::

    import twitterSentiment

    connection = twitterSentiment.API()
    search = connection.querySearch("Los Angeles", count=1, result_type='recent', lang='en')
    data = twitterSentiment.StructureStatusesData(search)
    sentiment = twitterSentiment.SentimentScore(data.getTweet())
    print(sentiment.getSentimentScore())

    >> 0.9824962449006399

Features
--------
* Connect to the tweeter API in a matter of seconds
* Get tweets sentiment score (ranges from -1 to 1)
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