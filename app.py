from archery import Archery
from army import Army
from bank import Bank
from barracks import Barracks
from market import Market
from stable import Stable
from building import Building


turn_counter = 0



class City(Building):
    
    def __init__(self, name, population, florins, bank, stable, archery, barracks, market, level, debt):
        Building.__init__(self, level, debt)
        self.name = name
        self.population = population
        self.level = 1
        self.florins = florins
        self.buildings = list()
        self.bank = bank
        self.barracks = barracks
        self.archery = archery
        self.stable = stable
        self.market = market
        self.army = []
        self.debt = 0
        
        
    

    def add_buildings(self, building):
        self.buildings.append(building)
   
    

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
    
    def calculate_debt(self, debt):
        new_amount = self.florins - self.debt
        self.florins = new_amount
        return new_amount
  

class Magistrate():
    def __init__(self, name):
        self.name = name

class Rival(City):


    def trade(self, amount):
        self.florins += amount




# (self, name, population, florins, bank, stable, archery, barracks, market, level, debt):

Epico = City("Epico", 10000, 1000, Bank(1,0), Stable(1,0), Archery(1,0), Barracks(1,0), Market(500, 1,0), 1,1)
army = Army(1000,1000,1000)
Epico.add_army(army)
print(army.horses)
Epico.add_buildings(Bank)
Epico.market.add_money(1000)
Epico.market.expand(Epico.market.level)
print(Epico.florins)
print(Epico.market.level)
Epico.calculate_debt(Epico.debt)
print(Epico.florins)



