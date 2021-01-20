class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_drinks_to_pub(self, drink):
        self.drinks.append(drink)
    
    def add_cash_to_till(self, amount):
        self.till += amount
        
    def age_check(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False
    def drunkenness_level(self, customer):
        if customer.drunkenness >= 2:
            return False
        else:
            return True

    def serve_drink(self, customer):
        old_enough = self.age_check(customer)
        sober_enough = self.drunkenness_level(customer)
        if old_enough == True:
            if sober_enough == True:
                return "What can I get you?"
            else:
                return "Your're done for the night."
        else:
            return "Get out youngling!"
       
        


      