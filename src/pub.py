class Pub:
    def __init__(self, name, till, drink):
        self.name = name
        self.till = till
        self.drink = drink

# check customer age
    def check_age(self, customer):
        if customer.age >= 18:
            return True

    #sell drink to customer - till goes up (call customer.buy_drink method from)
    def sell_drink(self, customer, drink_choice):
        if self.check_age(customer) == True:
            self.till += drink_choice.price
            customer.buy_drink(drink_choice)

    # add a function to refuse customer who has reached maximum drunk!
