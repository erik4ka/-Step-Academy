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
    def __init__(self):
        super().__init__("Spellsword", 20)
 
    def enchant_sword(self):
        print("Sword was successfully enchant on fire")
 
 
ss = SpellSword()
ss.rage()
print(ss.name)