import unittest

from src.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Connaught Bar", 100)

    
    def test_pub_has_name(self):
        self.assertEqual("The Connaught Bar", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    