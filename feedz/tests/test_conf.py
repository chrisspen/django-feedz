import unittest2 as unittest
from datetime import timedelta

from feedz import conf


class TestConf(unittest.TestCase):

    def test_interval(self):
        self.assertEqual(conf._interval(timedelta(seconds=10)),
                          timedelta(seconds=10))
        self.assertEqual(conf._interval(30), timedelta(seconds=30))
