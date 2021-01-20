import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Bawbag Beer", 5, 1)
    
    def test_drink_has_name(self):
        self.assertEqual("Bawbag Beer", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(5, self.drink.price)