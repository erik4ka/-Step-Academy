class Fruit:
    pass


class Tree:
    def __init__(self, height: int, trunk_width: int, leaf_color: str):
        self.height = height
        self.trunk_width = trunk_width
        self.leaf_color = leaf_color
        self.fruit_progress = 0

    def growth(self, value: int):
        self.height += value
        self.trunk_width += value / 10
        self.fruit_progress += value / 2

    def throw_off_fruit(self):
        return Fruit()


tree1 = Tree(100, 10, "yellow")
tree2 = Tree(125, 15, "red")
tree3 = Tree(140, 8, "green")
tree4 = Tree(300, 19, "green")
tree5 = Tree(1000, 100, "green")

tree1.growth(100)
