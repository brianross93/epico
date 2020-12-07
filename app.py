



class City:
    def __init__(self, name, population, florins, bank, stable, archery, barracks, market, level):
        self.name = name
        self.population = population
        self.level = level
        self.florins = florins
        self.buildings = list()
        self.bank = bank
        self.barracks = barracks
        self.archery = archery
        self.stable = stable
        self.army = []

    

    def add_buildings(self, building):
        self.buildings.append(building)

    def add_money(self, amount):
        added_florins = self.florins + amount
        self.florins = added_florins
        return added_florins

    def add_army(self, amount):
        self.army.append(amount)

    def add_horses(self, amount):
        added_horses = self.stable.make_horses(1000)
        self.population -= amount
        return added_horses

    def add_archers(self, amount):
        added_archers = self.archery.make_archers(1000)
        self.population -= amount
        return added_archers

    def add_infantry(self, amount):
        added_soldiers = self.barracks.make_soldiers(1000)
        self.population -= amount
        self.army.append(added_soldiers)
        return added_soldiers


    def collect_taxes(self, amount):
        self.florins += amount
        return self.florins
    
        

class Army:
    def __init__(self, horses, infantry, archers):
        self.horses = horses
        self.infantry = infantry
        self.archers = archers


class Stable():

    def __init__(self, amount):
        self.amount = amount
    

    def make_horses(self, amount):
        
        horse_army = Army(1000, 0, 0)
        print(horse_army.horses)
        return horse_army
        #can potentially make this change based on population size and stuff



class Barracks():
    
    def __init__(self, amount):
        self.amount = amount
    def make_soldiers(self, amount):
        man_army = Army(0,1000,0)
        print(man_army.infantry)
        return man_army

class Archery():

    def __init__(self, amount):
        self.amount = amount

    def make_archers(self, amount):
        shoot_army = Army(0, 0, 1000)
        print(shoot_army)
        return shoot_army

class Bank():

    def __init__(self, amount, interest):
        self.amount = amount
        self.interest = interest

class Market():

    def __init__(self, economy):
        self.economy = economy
    



class Magistrate:
    def __init__(self, name):
        self.name = name



# (self, name, population, florins, bank, stable, archery, barracks, market, level):

Epico = City("Epico", 10000, 1000, Bank(1000, 1.5), Stable(1000), Archery(1000), Barracks(1000), Market(500), 1 )
army = Army(1000,1000,1000)
Epico.add_army(army)
print(Epico.army)
Epico.add_buildings(Bank)
Epico.add_money(1000)
Epico.add_infantry(1000)

