import unittest

from src.customer import Customer
from src.pub import Pub
from src.food import Food
from src.drink import Drink

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food_1 = Food("Crisps", 1, 1)
        self.food_2 = Food("Steak Pie", 2, 2)
        self.customer_1 = Customer("James", 50, 38)
        self.drink_1 = Drink("Bawbag Beer", 5, 2)
    
    def test_has_food(self):
        self.assertEqual("Crisps", self.food_1.name)
    
    def test_buy_food(self):
        self.customer_1.buy_food(self.food_1)
        self.assertEqual(1, len(self.customer_1.purchased_food))

    def test_consumes_food(self):
        self.customer_1.increase_drunkenness(self.drink_1)
        self.food_1.consume_food(self.customer_1, self.food_1)
        self.assertEqual(1, self.customer_1.drunkenness)