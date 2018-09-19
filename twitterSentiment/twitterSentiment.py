import requests
from urllib.parse import urlencode
import base64
import json
import datetime 
import os
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
import re

class API(object):
    """
    Create an API object that will handle connection, search request, and response.
    We use OAuth client integration flow and use a bearer token for our request to the twitter search API.

    Since the flow does not ask the user to authorize the app, this library will only have access to the 
    publicly available data (i.e. public tweets and public profiles).

    IMPORTANT
    ---------
    For the library to work, you will need to create 2 environment variables "CLIENT_KEY" and "CLIENT_SECRET"
    that will hold your client_key and client_secret from your app.

    """

    def __init__(self):
        self.client_key = os.environ.get("TWITTER_CLIENT_KEY")
        self.client_secret = os.environ.get("TWITTER_CLIENT_SECRET")
        self.base_url = "https://api.twitter.com/"
        self.token_url_extension = 'oauth2/token'
        self.search_url_extension = '1.1/search/tweets.json?'

    def getBearerToken(self):
        """
        Handle the OAuth client integration flow and returns a string containing the parameter for the 
        HTTP Authorization header
        """
        ## Prepare authorization header for twitter authentification server request
        concatenated_string = ':'.join([self.client_key,self.client_secret])
        base_64 = base64.b64encode(bytes(concatenated_string, 'utf-8')) ## string needs to be converted to bytes for base64 encoding
        base_64 = base_64.decode("utf-8") ## convert bytes to utf-8 string for request
        authorization_url = self.base_url + self.token_url_extension
        payload = {'grant_type':'client_credentials'}
        headers = {'Authorization':'Basic ' + base_64, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
        
        ## Execute post request to the bearer token
        request = requests.post(authorization_url, data=payload, headers=headers)

        ## Response comes back as a string. Convert it to a json type to access the "access_token" field
        response = json.loads(request.text)
        access_token = response['access_token']

        return f'Bearer {access_token}'
        

    def querySearch(self, q=None, geocode=None, lang=None, result_type='mixed', count=15, until=None, since_id=None, max_id=None, include_entities=False, tweet_mode="extended", return_json=True):
        """

        """
        self.search_url = self.base_url + self.search_url_extension
        self.params = []
        if (q == None or q == "") and not geocode:
            raise ValueError("Invalid request. You must provide a search term")
        elif (q == None or q == ""):
            pass
        else:
            val = urlencode({"q":q})
            self.params.append(val)

        if geocode:
            self.params.append(f'geocode={geocode}')

        if count != 15 or count != None:
            count = urlencode({"count":count})
            self.params.append(count)
        
        if lang:
            self.params.append(f'lang={lang}')

        if result_type != "mixed":
            if result_type == "recent" or result_type == "popular":
                self.params.append(f'result_type={result_type}')
            else:
                raise ValueError(f"result_type {result_type} is not a valid parameter. Make sure to use either 'mixed', 'recent', or 'popular'")
        
        if until:
            if datetime.datetime.strptime(until, '%Y-%m-%d'):
                self.params.append(f'until={until}')
            else:
                raise ValueError("Invalide date format. Please make sure to use a date format 'YYYY-MM-DD'") 

        if since_id:
            self.params.append(f'since_id={since_id}')

        if max_id:
            self.params.append(f'max_id={max_id}')

        if tweet_mode == "extended":
            self.params.append(f'tweet_mode={tweet_mode}')

        if include_entities:
            self.params.append(f'include_entities={include_entities}')

        for parameter in self.params:
            if 'q' in parameter:
                self.search_url += parameter
            elif not 'q' in self.params[0] and 'geocode' in parameter:
                self.search_url += parameter 
            else:
                self.search_url += f'&{parameter}'

        ## Prepare header for request
        headers = {"Authorization": self.getBearerToken()}
        ## Execute request
        statuses = requests.get(self.search_url, headers=headers)

        if return_json:
            statuses = json.loads(statuses.text)
            return statuses
        else:
            return statuses.text

class StructureStatusesData(object):
    """
    Creates an object that will handle data formating. structureStatusesData object takes a twitter statuses
    returned from the querySearch method of the API object

    This object structures data into 3 lists each containing dictionnary with the following data:
        1) tweets
            - id -> PRIMARY KEY
            - created_at
            - full_text
            - geo
            - coordinates
            - place
            - retweet_count
            - favorite_count
            - entities
                - hashtags
                - user_mentiones
                    - id -> FOREIGN KEY
            - metadata
                - iso_language_code
            - user
                - id -> FOREIGN KEY
        
        2) user_mentioned
            - tweet_id -> PRIMARY KEY / FOREIGN KEY
            - entities
                - user_mentions
                    - id -> FOREIGN KEY
                    - name
                    - screen_name
        
        3) user
            - user
                - id
                - name
                - screen_name
                - location
                - description
                - followers_count
                - friends_count
                - listed_count
                - favourites_count
                - verified
                - statuses_count
                - lang

        Below is a schema of potential joining key if data are implemented into a database
        
        tweets                                                                          user_mentioned
          |________________________(tweets.id = user_mentioned.tweet_id)________________________|
          |____(tweets.entities.user_mentiones.id = user_mentions.entities.user_mentions.id)____|
        tweets                                  user
          |____(tweets.user.id = user.user.id)____|

    """

    def __init__ (self, statuses):
        self.statuses = statuses
    
    def getData(self):
        user = []
        user_mentioned = []
        tweets = []
        i = 0
        for elements in self.statuses["statuses"]:
            
            tweets.append({
                            "id":elements["id"],
                            "created_at":elements["created_at"],
                            "full_text":elements["full_text"],
                            "geo":elements["geo"],
                            "coordinates":elements["coordinates"],
                            "place":elements["place"],
                            "retweet_count":elements["retweet_count"],
                            "favorite_count":elements["favorite_count"],
                            "entities":{"hashtags":elements["entities"]["hashtags"]},
                            "metadata":{"iso_language_code":elements["metadata"]["iso_language_code"]},
                            "user":{"id":elements["user"]["id"]}
            })

            if elements["entities"]:
                if len(elements["entities"]["user_mentions"]) > 0:
                    tweets[i]["entities"] = {'user_mentiones': {"id":elements["entities"]["user_mentions"][0]["id"]}}
                    user_mentioned.append({
                            "tweet_id":elements["id"],
                            "entities":{"user_mentions":{"id":elements["entities"]["user_mentions"][0]["id"],
                            "name":elements["entities"]["user_mentions"][0]["name"],
                            "screen_name":elements["entities"]["user_mentions"][0]["screen_name"]}}
                    })

                else:
                    tweets[i]["entities"] = "NULL"
                    user_mentioned.append({
                            "NULL",
                            "NULL",
                    })   

            user.append({
                    "id":elements["user"]["id"],
                    "name":elements["user"]["name"],
                    "screen_name":elements["user"]["screen_name"],
                    "location":elements["user"]["location"],
                    "description":elements["user"]["description"],
                    "followers_count":elements["user"]["followers_count"],
                    "friends_count":elements["user"]["friends_count"],
                    "listed_count":elements["user"]["listed_count"],
                    "favourites_count":elements["user"]["favourites_count"],
                    "verified":elements["user"]["verified"],
                    "statuses_count":elements["user"]["statuses_count"],
                    "lang":elements["user"]["lang"]
            })

            i += 1

        return user, user_mentioned, tweets

    def getTweet(self):
        tweets = self.getData()[2]
        return tweets

    def getUser(self):
        user = self.getData()[0]
        return user
    
    def getUserMentioned(self):
        user_mentioned = self.getData()[1]
        return user_mentioned

class SentimentScore(object):

    def __init__(self, tweet_list):
        pattern = re.compile(r'https:\/\/[\w\d\.\-\/]+')
        self.tweet_list = []

        for status in tweet_list:
            cleaned_status = re.sub(pattern,'', status["full_text"]) # remove URLs from tweet
            self.tweet_list.append(cleaned_status)

        self.blobber = Blobber(analyzer=NaiveBayesAnalyzer())

    def getSentimentClassification(self):
        sentiment_classification = []

        for el in self.tweet_list:
            blob = self.blobber(el)
            score = blob.sentiment
            if score[0] == 'pos':
                sentiment_classification.append(1)
            else:
                sentiment_classification.append(0)

        return sum(sentiment_classification)/len(sentiment_classification)


    