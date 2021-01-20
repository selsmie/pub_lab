import unittest

from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Connaught Bar", 100)
        self.drink_1 = Drink("Bawbag Beer", 5)
        self.drink_2 = Drink("Champs Lager", 4)
        

    
    def test_pub_has_name(self):
        self.assertEqual("The Connaught Bar", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_pub_has_drink(self):
        self.pub.add_drinks_to_pub(self.drink_1)
        self.assertEqual(1, len(self.pub.drinks))

    def test_add_cash_to_till(self):
        self.pub.add_cash_to_till(5)
        self.assertEqual(105, self.pub.till)


    