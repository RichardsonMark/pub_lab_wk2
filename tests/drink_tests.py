import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("House wine", 7)


#    @unittest.skip("Delete this line to run the test")
    def test_drink_has_name(self):
        self.assertEqual("House wine", self.drink.name)

#    @unittest.skip("Delete this line to run the test")
    def test_drink_has_price(self):
        self.assertEqual(7, self.drink.price)