from building import Building
from army import Army

class Archery(Building):

    def make_archers(self, amount):
        shoot_army = Army(0, 0, 1000)
        print(shoot_army)
        return shoot_army