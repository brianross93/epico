from building import Building
from army import Army

class Market(Building):
    def __init__(self, economy, level, debt):
        Building.__init__(self, level, debt)
        self.economy = economy
        self.level = level
        self.debt = debt
        

    def add_money(self, amount):
        added_florins = self.economy * (self.level * 1.5)
        print(f"Market has given {added_florins} florins in tax revenue ")
        return added_florins

    def expand(self, level):
        money_q = input("Do you want to expand the market for 1000 florins? Press 1 for Yes and 2 for No ")

        if money_q == "1":
            self.level += 1
            self.debt += 1000
            print("You have expanded the market!")
        
        else: 
            print("You have not expanded the market")