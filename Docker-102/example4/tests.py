import unittest
import requests

API_URL = "http://api:5000/"


class TestGet(unittest.TestCase):
    def runTest(self):
        r = requests.get(API_URL)
        self.assertEqual(r.status_code, 200)


class TestPost(unittest.TestCase):
    def runTest(self):
        r = requests.post(API_URL, data = "dummy data")
        self.assertEqual(r.status_code, 200)

