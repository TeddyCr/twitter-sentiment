===============
Getting Started
===============

Getting Twitter Access Token
----------------------------
Before you can send requests to the Twitter API you will need to create an application and get credentials. Credentials are composed of Consumer key, Access Token and Access Token Secret.

You can find more information on how to create an application `here <https://developer.twitter.com/en/docs/basics/getting-started>`

Creation Environment Variable
-----------------------------
Once you have your credentials you will need to create environment variables referencing your API Key and your API Secret Key. This is important as it 1) keep those two private and unexposed to whomever you will share your code with 2) allows you to send requests to the Twitter API.

**On Mac**
Open your terminal and enter the following command

::

    nano .bash_profile

Once your .bash_profile is open, create two environment variables by entering the following text

::

    export TWITTER_CLIENT_KEY="your_api_key"
    export TWITTER_CLIENT_SECRET="your_api_secret_key"
