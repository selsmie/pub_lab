class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_drinks_to_pub(self, drink):
        self.drinks.append(drink)
    
    def add_cash_to_till(self, amount):
        self.till += amount