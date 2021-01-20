import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("James", 50)
        self.drink_1 = Drink("Bawbag Beer", 5)

    def test_customer_name(self):
        self.assertEqual("James", self.customer.name)

    def test_customer_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_remove_cash_from_wallet(self):
        self.customer.remove_cash_from_wallet(5)
        self.assertEqual(45, self.customer.wallet)
    
    def test_customer_buys_drink(self):
        self.customer.customer_buys_drink(self.drink_1)
        self.assertEqual(45, self.customer.wallet)
        self.assertEqual(105, Pub.till)
        self.assertEqual(1, len(self.customer.purchased_drink))

