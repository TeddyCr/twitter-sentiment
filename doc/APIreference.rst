=============
API Reference
=============

API Class
---------
This classe is directly imported from twitterSentiment. It handles the basic connection to the API as well as tweet searches.

::

    from twitterSentiment import API

**twitterSentiment.API()** - *API object*  
    the API() class manage the connection to the Tweeter API. API() does not take any parameter, though, it is required to create a `TWITTER_CLIENT_KEY` and `TWITTER_CLIENT_SECRET` environment variable in your system to connect to your Twitter application. It is required to create an API object before calling any of the class methods.


**getBearerToken()** - *string*
    Returns a string object referencing the value of the bearer token. It is used in searchQuery() class method to authorize the request to the Twitter API.


**searchQuery()** - *dictionnary*
    It is the main class to send search query to the Twitter API. It returns a dictionnary object. The class has 11 parameters:
        * **q** - a string. This is where the search keyword is passed [REQUIRED - optional if geocode is not specified]
        * **geocode** - a string composed of 3 values separated by comas (lat, long, radius). Radius needs to be specified in either miles or kilometer by passing "mi" or "km" [OPTIONAL - required if q not specified]
        * **lang** - a string representing the language filter for the tweets to return [OPTIONAL]
        * **result_type** - a string. This parameter accepts only 2 values "mixed" or "recent" [REQUIRED]
        * **count** - integer. The number of tweets to return per request. Default to 15 [REQUIRED]
        * **until** - [OPTIONAL]
        * **since_id** - [OPTIONAL]
        * **max_id** - [OPTIONAL]
        * **include_entities** - [OPTIONAL]
        * **tweet_mode** - a string. Default to "extended" [REQUIRED]
        * **return_json** - a string. Format of the response. Default to "JSON". Changing this argument may yield unexpected results [REQUIRED]


**client_key** - *string*
    Will return the client key value saved in the environment variable.


**client_secret** - *string*
    Will return the client secret value saved in the environement variable.


**base_url** - *string*
    Will return the main root of the API URL.


**token_url_extension** - *string*
    Will return the API URL extension for the token autorization.


**search_url_extension** - *string*
    Will return the API URL extension used for the request (default to the standard API `1.1/search/tweets.json?`).


**self.search_url** - *string*
    Will return the full search URL used for the request.


**self.params** - *list*
    Will return the list of parameters to pass to the search_url.


StructureStatusesData Class
----------------------------
This class is directly imported from twitterSentiment. It is use to get a list of formated data with only specific data points - as opposed to the raw json response returned by `twitterSentiment.searchQuery()`.

::

    form twitterSentiment import StructureStatusesData

**twitterSentiment.StructureStatusesData()** - *StructureStatusesData object*
    Takes one argument. The argument should be the value returned by the `searchQuery()` class method of `API()`. The raw response returned by the twitter API should also work - though unexpected behaviors could happen.

**getData()** - *list*
    Returns a list of length 3 comprised of sub list of length equals to the `count` argument value from `twitterSentiment.searchQuery()`.


**getTweet()** - *list*
    Returns a list of length `count` with tweets values. The values returned by `getTweet()` are:
        * id
        * created_at
        * full_text
        * geo
        * coordinates
        * place
        * retweet_count
        * favorite_count
        * entities
            * hashtags
            * user_mentiones
                * id
        * metadata
            * iso_language_code
        * user
            * id


**getUser()** - *list*
    Returns a list of length `count` with tweets values. The values returned by `getUser()` are:
        * user
            * id
            * name
            * screen_name
            * location
            * description
            * followers_count
            * friends_count
            * listed_count
            * favourites_count
            * verified
            * statuses_count
            * lang


**getUserMentioned()** - *list*
    Returns a list of length `count` with tweets values. The values returned by `getUserMentioned()` are:
        * tweet_id
        * entities
            * user_mentions
                * id
                * name
                * screen_name

**self.statuses** - *dictionnary*
    Returns the raw response from the API request.

SentimentScore Class
---------------------
This class is directly imported from twitterSentiment. It is used to classify a list of tweets returned by `twitterSentiment.StructureStatusesData().getTweet()`.  

::

    form twitterSentiment import StructureStatusesData

**twitterSentiment.SentimentScore()** - *SentimentScore object*
    Takes the value returned by `getTweet()` as an argument.


**getSentimentClassification()** - *float*
    Returns the ratio of tweets classified as positive by TextBlob `NaiveBayesAnalyzer()` model.

**self.tweet_list** - *list*
    Returns a list of tweets without any URLs. Cleaned up for sentiment analysis.

**self.blobber** - *Blobber Class*
    Returns a blobber class. Initialized to prevent retraining of model for each tweet analyzed.