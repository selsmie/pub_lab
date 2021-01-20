class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.purchased_drink = []
    
    def buy_drink(self, drink_name):
        self.purchased_drink.append(drink_name)

    def remove_cash_from_wallet(self, amount):
        self.wallet -= amount

    def customer_buys_drink(self, drink):
        self.buy_drink(drink)
        self.remove_cash_from_wallet(drink.price)
        pub.add_cash_to_till(drink.price)

    