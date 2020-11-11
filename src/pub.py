class Pub:
    def __init__(self, name, till, drink):
        self.name = name
        self.till = till
        self.drink = drink

    #sell drink to customer - till goes up (call customer.buy_drink method from)

    def sell_drink(self, customer, drink_choice):
        self.till += drink_choice.price
        customer.buy_drink(drink_choice)