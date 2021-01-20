class Food:
    def __init__(self, name, price, rejuvenation_level):
        self.name = name
        self.price = price
        self.rejuvenation_level = rejuvenation_level

    def consume_food(self, customer, food):
        customer.drunkenness -= self.rejuvenation_level
        if customer.drunkenness < 0:
            customer.drunkenness = 0