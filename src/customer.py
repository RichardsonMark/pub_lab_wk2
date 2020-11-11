class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    # buys drink - money goes down
    def buy_drink(self, drink_choice):
        self.wallet -= drink_choice.price


 
    