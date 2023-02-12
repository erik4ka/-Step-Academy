class Basic_Class:
    def __init__(self, name, points):
        self.name = name
        self.points = points
 
    def teleport(self):
        print("Teleporting")
 
 
class Warrior():
    def __init__(self, name, points):
        self.name = name
        self.points = points
 
    def sword_attack(self):
        print("Sword Attack")
 
    def rage(self):
        print("Rage")
 
 
class Mage():
    def __init__(self, name, points):
        self.name = name
        self.points = points
 
    def fireball(self):
        print("Fireball")
 
    def icewall(self):
        print("Icewall")
 
 
class Archer():
    def __init__(self, name, points):
        self.name = name
        self.points = points
 
    def trap(self):
        print("Trap")
 
    def invisibility(self):
        print("Invisibility")
 
 
class SpellSword(Warrior, Mage):
    def __init__(self, name="Spellsword", points=20):
        super().__init__(name, points)
 
    def enchant_sword(self):
        print("Sword was successfully enchant on fire")
 
 
class Pathfinder(Warrior, Archer):
    def __init__(self, name="Pathfinder", points=10):
        super().__init__(name, points)
 
    def toss_dagger(self):
        print("Dagger toss")
 
 
class ElementalArcher(Mage, Archer):
    def __init__(self, name="ElementalArcher", points=15):
        super().__init__(name, points)
 
    def elemental_arrow(self):
        print("Element arrow")
 
 
class Hero(ElementalArcher, Pathfinder, SpellSword):
    def __init__(self, name="Hero", points=50):
        super().__init__(name, points)
 
    def weapon_world(self):
        print("weapon_world")
 
 
ss = Hero()
ss.rage()
ss.fireball()
ss.enchant_sword()
ss.print(ss.name)
 