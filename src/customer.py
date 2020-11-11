class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    # buys drink - money goes down
    def buy_drink(self, drink_choice):
        self.wallet -= drink_choice.price

    