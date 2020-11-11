import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Andrew Carnegie", 30)

    # @unittest.skip("Delete this line to run the test")
    def test_customer_has_name(self):
        self.assertEqual("Andrew Carnegie", self.customer.name)

    # @unittest.skip("Delete this line to run the test")
    def test_customer_has_cash(self):
        self.assertEqual(30, self.customer.wallet)

    # @unittest.skip("Delete this line to run the test")
    def test_customer_can_buy_drink(self):
        drink_choice = Drink("House wine", 7)
        self.customer.buy_drink(drink_choice)
        self.assertEqual(23, self.customer.wallet)

