=============
API Reference
=============

API Class
---------

This classes is directly imported from twitterSentiment. It handles the basic connection to the API as well as tweet searches

::

    from twitterSentiment import API

**twitterSentiment.API()**
    the API() class manage the connection to the Tweeter API. API() does not take any parameter, though, it is required to create a `TWITTER_CLIENT_KEY` and `TWITTER_CLIENT_SECRET` environment variable in your system to connect to your Twitter application. It is required to create an API object before calling any of the class methods.


**getBearerToken()**
    Returns a string object referencing the value of the bearer token. Used in searchQuery() class method to authorize the request to the Twitter API


**searchQuery()**
    It is the main class to send search query to the Twitter API. It returns a dictionnary object. The class has 11 parameters:

        * **q** - a string. This is where the search keyword is passed [REQUIRED]
        * **geocode** - a tuple containing 3 values


**client_key**
    Will return the client key value saved in the environment variable


**client_secret**
    Will return the client secret value saved in the environement variable


**base_url**
    Will return the main root of the API URL


**token_url_extension**
    Will return the API URL extension for the token autorization


**search_url_extension**
    Will return the API URL extension used for the request (default to the standard API `1.1/search/tweets.json?`)


**self.search_url**
    Will return the full search URL used for the request


**self.params**
    Will return the list of parameters to pass to the search_url