import unittest
import sys
import requests
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import twitter_api

class testTwitterAPICall(unittest.TestCase):

    def setUp(self):
        self.connection = twitter_api.API()
        self.base_url = self.connection.base_url
        self.search_url_extension = self.connection.search_url_extension

    def testAPIRequest(self):
        headers = {"Authorization": self.connection.getBearerToken()}
        search_url = self.base_url + self.search_url_extension + "q=los%20Angeles"
        r = requests.get(search_url, headers=headers)
        self.assertEqual(200, r.status_code)

    def testQueryArgumentValidation(self):
        """
        if query argument is not present in querySearch, it should raise Value Error
        """
        with self.assertRaises(ValueError) as err:
            self.connection.querySearch()

    def testQuerySearchType(self):
        search_json = self.connection.querySearch("test", count=1, return_json=True)
        search_string = self.connection.querySearch("test", count=1, return_json=False)
        with self.subTest():
            self.assertIsInstance(search_json,dict)
            self.assertIsInstance(search_string,str)

if __name__ == '__main__':
    unittest.main()