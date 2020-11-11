import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink_1 =  Drink("Super T", 3)
        self.drink_2 =  Drink("Buckfast", 5)
        self.drink_3 =  Drink("Mysterious Cocktail", 4)
        self.drink_4 =  Drink("House wine", 7)
        
        drinks = [self.drink_1, self.drink_2, self.drink_3, self.drink_4,]

        self.pub = Pub("One way Tolbooth", 500, drinks)         
        self.customer = Customer("Andrew Carnegie", 30)

#    @unittest.skip("Delete this line to run the test")
    def test_has_pub_name(self):
        self.assertEqual("One way Tolbooth", self.pub.name)

#    @unittest.skip("Delete this line to run the test")
    def test_has_till(self):
        self.assertEqual(500, self.pub.till)

    # @unittest.skip("Delete this line to run the test")
    def test_can_sell_drink_to_customer(self):
        self.pub.sell_drink(self.customer, self.drink_2)
        self.assertEqual(505, self.pub.till)
        self.assertEqual(25, self.customer.wallet)
