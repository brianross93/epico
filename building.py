

class Building:
    def __init__(self, level, debt):
        self.level = level
        self.debt = debt
    
    def give_values(self, level, debt):
        debt = self.debt
        level = self.level
        return debt, level


    