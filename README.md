Python library to Explore Emotions Behind Tweets
================================================

twitter-sentiment is a Python library leveraging NLP algorithm and the Twitter API to classify the sentiment of a tweet.

Installation 
------------ 
Installing twitter-sentiment is simple, you just have to use pip.
::

    pip install twitter-sentiment


Documentation
-------------  
Documentation is available at [twitter-sentiment.readthedocs.io](https://twitter-sentiment.readthedocs.io/en/latest/index.html)

twitter-sentiment in a nutshell
------------------------------
twitter-sentiment let you classify a tweet/list of tweets as positive (1) or negative (0). twitter-sentiment then calculate and returns the ration of positive tweets. To classify a tweet, twitter-sentiment leverage TextBlob Naive Bayes NLP library. More information can be find at [textblob.readthedocs.io](https://textblob.readthedocs.io/en/dev/advanced_usage.html#sentiment-analyzers)

Continuous Integration
---------------------
twitter-sentiment uses circleci as a continuous integration tool. Pushing a new git tag to the remote repository will trigger circleci workflow and:
* validate the test in /test/test_twitterSentiment.py
* check for a match between the `VERSION` variable in the setup.py file and the git tag version. 

If all tests pass, the build will be automatically uploaded to the pypi server
