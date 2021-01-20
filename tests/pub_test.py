import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Connaught Bar", 100)
        self.drink_1 = Drink("Bawbag Beer", 5, 1)
        self.drink_2 = Drink("Champs Lager", 4, 1)
        self.customer_1 = Customer("James", 50, 38)
        self.customer_2 = Customer("Simon", 50, 16)
    
    def test_pub_has_name(self):
        self.assertEqual("The Connaught Bar", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    @unittest.skip
    def test_pub_has_drink(self):
        self.pub.add_drinks_to_pub(self.drink_1)
        self.assertEqual(1, len(self.pub.drinks))

    def test_add_cash_to_till(self):
        self.pub.add_cash_to_till(5)
        self.assertEqual(105, self.pub.till)

    def test_age_check_fail(self):
        self.assertEqual(False, self.pub.age_check(self.customer_2))

    def test_age_check_pass(self):
        self.assertEqual(True, self.pub.age_check(self.customer_1))
    
    def test_drunkenness_level_fail(self):
        self.customer_1.increase_drunkenness(self.drink_1)
        self.customer_1.increase_drunkenness(self.drink_2)
        self.assertEqual(False, self.pub.drunkenness_level(self.customer_1))

    def test_drunkenness_level_pass(self):
        self.assertEqual(True, self.pub.drunkenness_level(self.customer_2))

    def test_serve_drink_pass(self):
        self.assertEqual("What can I get you?", self.pub.serve_drink(self.customer_1))
    
    def test_serve_drink_fail(self):
        self.customer_1.increase_drunkenness(self.drink_1)
        self.customer_1.increase_drunkenness(self.drink_2)
        self.assertEqual("Your're done for the night.", self.pub.serve_drink(self.customer_1))

    def test_serve_drink_young(self):
        self.assertEqual("Get out youngling!", self.pub.serve_drink(self.customer_2))

    def test_add_to_stock(self):
        self.pub.add_drinks_to_stock(self.drink_1.name, 2)
        self.assertEqual(True, "Bawbag Beer" in self.pub.drinks)
        
    def test_stock_take(self):
        self.pub.add_drinks_to_stock(self.drink_1.name, 2)
        self.pub.add_drinks_to_stock(self.drink_2.name, 3)
        self.assertEqual(5, self.pub.stock_take())
    
    # def test_stock_value(self):
    #     self.pub.add_drinks_to_stock(self.drink_1, 2)
    #     self.pub.add_drinks_to_stock(self.drink_2, 3)
    #     self.assertEqual(22, self.pub.stock_value())