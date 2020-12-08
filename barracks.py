from building import Building
from army import Army

class Barracks(Building):

    
    def make_soldiers(self, amount):
        man_army = Army(0,1000,0)
        
        print(man_army.infantry)
        return man_army