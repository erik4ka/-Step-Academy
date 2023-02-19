class InteriorItem:
    def __init__(self, name, material, color):
        self.name = name
        self.material = material
        self.color = color

class Sofa(InteriorItem):
    def __init__(self, name, material, color, seats):
        super().__init__(name, material, color)
        self.seats = seats

class Table(InteriorItem):
    def __init__(self, name, material, color, shape):
        super().__init__(name, material, color)
        self.shape = shape