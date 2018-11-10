import unittest
import sys
import requests
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import twitterSentiment


class testTwitterAPICall(unittest.TestCase):

    def setUp(self):
        count = 1
        self.connection = twitterSentiment.API()
        self.base_url = self.connection.base_url
        self.search_url_extension = self.connection.search_url_extension
        self.search = self.connection.querySearch(q="Los Angeles", count=count)

    def testAPIRequest(self):
        headers = {"Authorization": self.connection.getBearerToken()}
        search_url = self.base_url + \
            self.search_url_extension + "q=los%20Angeles"
        r = requests.get(search_url, headers=headers)
        self.assertEqual(200, r.status_code)

    def testQueryArgumentValidation(self):
        """
        if query argument is not present in querySearch,
        it should raise Value Error.
        """
        with self.assertRaises(ValueError) as _:
            self.connection.querySearch()

    def testQuerySearchType(self):
        search_json = self.connection.querySearch(
            "test", count=1, return_json=True)
        search_string = self.connection.querySearch(
            "test", count=1, return_json=False)
        with self.subTest():
            self.assertIsInstance(search_json, dict)
            self.assertIsInstance(search_string, str)

    def testGetData(self):
        structured_data = twitterSentiment.StructureStatusesData(self.search)
        data = structured_data.getData()
        self.assertEqual(3, len(data))

    def testGetTweets(self):
        structured_data = twitterSentiment.StructureStatusesData(self.search)
        tweet = structured_data.getTweet()
        self.assertGreaterEqual(11, len(tweet[0]))

    def testGetUser(self):
        structured_data = twitterSentiment.StructureStatusesData(self.search)
        user = structured_data.getUser()
        self.assertEqual(12, len(user[0]))


if __name__ == '__main__':
    unittest.main()
