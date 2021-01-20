import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("James", 50)

    def test_customer_name(self):
        self.assertEqual("James", self.customer.name)

    def test_customer_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_customer_buy_drink(self):
        self.assertEqual(1, self.customer.purchased_drink)