class Basic_Class:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def teleport(self):
        print("Teleporting")


class Warrior(Basic_Class):
    # sword_attack
    # rage


class Mage(Basic_Class):
    def __init__(self):
        super("Mage", 10)

    # fireball
    # icewall


class Archer(Basic_Class):

    # trap
    # invisible
