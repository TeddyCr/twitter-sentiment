import unittest
import twitter_api
import twitter

class testTwitterAPICall(unittest.TestCase):

    def setUp(self):
        connection = twitter_api.querySearch("", "", "", "")
        self.search = connection.make_search_query_request(geocode=("34.052235", "-118.243683", "15mi"), count=2, result_type="recent", include_entities=True)
        self.data = twitter_api.structureQueryData(self.search)

    def test_get_data(self):
        result = self.data.getData()
        self.assertEqual(3, len(result))

    def test_get_Tweets(self):
        tweet = self.data.getTweet()
        with self.subTest():
            self.assertEqual(2,len(tweet)) ## Should return the same lenght than the amount of tweets parsed
            self.assertEqual(11,len(tweet[0]))

    def test_get_user(self):
        user = self.data.getUser()
        with self.subTest():
            self.assertEqual(2,len(user)) ## Should return the same lenght than the amount of tweets parsed
            self.assertEqual(12, len(user[0]))

    def test_get_user_mentioned(self):
        user_mentioned = self.data.getUserMentioned()
        with self.subTest():
            self.assertEqual(2,len(user_mentioned)) ## Should return the same lenght than the amount of tweets parsed
            self.assertEqual(3, len(user_mentioned[0]))

if __name__ == '__main__':
    unittest.main()