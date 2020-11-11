class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        # add drunkeness level (theoretically 0)

    # buys drink - money goes down
    def buy_drink(self, drink_choice):
        self.wallet -= drink_choice.price
    # add to function, each drink increases alcohol/drunkeness level

 
    