from building import Building
from army import Army
class Stable(Building):

    def make_horses(self, amount):
        
        horse_army = Army(1000, 0, 0)
        print(horse_army.horses)
        return horse_army
        #can potentially make this change based on population size and stuff
    