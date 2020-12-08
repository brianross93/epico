from building import Building
from army import Army

class Bank(Building):

    def add_interest(self, amount, interest):
        self.amount = amount
        self.interest = interest
        added_interest = (self.amount * self.interest)
        return added_interest