===============
Getting Started
===============

Getting Twitter Access Token
----------------------------
Before you can send requests to the Twitter API you will need to create an application and generate credentials. Credentials are composed of Consumer key, Access Token and Access Token Secret.

You can find more information on how to create an application `here <https://developer.twitter.com/en/docs/basics/getting-started>`_

Creating an Environment Variable
--------------------------------
Once you have your credentials you will need to create two environment variables referencing your API Key and your API Secret Key. This is important as it 1) keep those two keys private and unexposed to whomever you will share your code with and 2) allows you to send requests to the Twitter API.

**On Mac**

Open your terminal and enter the following command

::

    nano .bash_profile

Once your .bash_profile is open, create two environment variables by entering the following text. Make sure you do not include spaces between the "=" and your variable name and values.

::

    export TWITTER_CLIENT_KEY="your_api_key"
    export TWITTER_CLIENT_SECRET="your_api_secret_key"

**On Windows**

Current version has not been tested on Windows.

Creating an API Object
----------------------

The first step is to create an `API()` object that will handle the connection to the Twitter API.

::

    api = twitterSentiment.API()

Searching Tweets
----------------

Once you have instantiated an `API()` object you will be able to search for tweets by using the `searchQuery()` method.

::

    tweet = api.searchQuery('Twitter', geocode=None,lang='en',result_type='recent' ,count=1, until=None, since_id=None, max_id=None, include_entities=False, tweet_mode="extended", return_json=True)

    print(tweet)

    >> {'statuses': [{'created_at': 'Thu Sep 06 19:38:16 +0000 2018', 'id': 1037787081936973824, 'id_str': '1037787081936973824', 'full_text': ....

`searchQuery()` returns a dictionnary with 1 key and 1 value. The value of the dictionnary is a list with one dictionnary per count of tweets returned.

Getting Structured Data
-----------------------

Once you have your tweet(s), you can create an object `StructureStatusesData()` to get the data in a structured way. `StructureStatusesData()` takes one argument, which is the value returned by the `searchQquery()` method. 4 methods can be used with `StructureStatusesData()`:

* getData()
* getTweet()
* getUser()
* getUserMentioned()

::

    data = twitterSentiment.StructureStatusesData(tweet)
    structured_tweets = data.getTweet()
    print(data.getData())

    >> ([{id': 856800998, 'name': 'Someone', 'screen_name': 'some_one', ....}])

The getData() method is the most general one. It returns a tuple of length 3 composed of list, each holding tweets, user, and user mentions data. Each list contains a dictionnary per `count` of tweets defined in the searchQuery() method 

Getting Sentiment Classification Ratio
--------------------------------------

With your tweets structured into a list, you can use the `getTweet()` class method to easily get the ratio of positively classified tweets in your returned values.

::

    sentiment = twitterSentiment.SentimentScore(structured_tweets)
    print(sentiment.getSentimentClassification())

    >> 0.6666