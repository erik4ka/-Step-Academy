# Этажи подземелья хранятся в плеере, как уровень
# У плеера может быть меч, броня и 3 скилла
# У плеера есть атака и хп и инвентарь
# У брони будет прочность и кол-во поглащаемого урона
# У оружие будет атака и прочность
# У монстра будет атака и хп и броня на 1 удар

import random


class Weapon:
    def __init__(self, name: str, offense: int):
        self.name = name
        self.offense = offense


class Armor:
    def __init__(self, name: str, defense: int, endurance: int):
        self.name = name
        self.defense = defense
        self.endurance = endurance


class Spell:
    def __init__(self, name: str, value: int, type: str):
        self.name = name
        self.value = value
        self.type = type

    def use(self, caster, target=None):
        if self.type == "damage":
            if target:
                target.hp -= self.value
            else:
                caster.hp -= self.value
        if self.type == "heal":
            caster.hp += self.value


class Player:
    def __init__(self, name: str, hp: int, offense: int):
        self.name = name
        self.hp = hp
        self.offense = offense
        self.level = 0
        self.weapon: Weapon = None
        self.armor: Armor = None
        self.spells: dict[Spell] = {1: None, 2: None, 3: None}
        self.inventory = {1: None, 2: None, 3: None, 4: None, 5: None}

    def attack(self, target):
        summary_offense = self.offense
        if self.weapon:
            summary_offense += self.weapon.offense
        damage = target.defense - summary_offense
        target.defense -= summary_offense
        if target.defense <= 0:
            target.defense = 0
        if damage > 0:
            target.hp -= damage

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def change_armor(self, new_armor: Armor):
        self.armor = new_armor

    def add_to_inventory(self, item: Weapon | Armor):
        for place, key in self.inventory:
            if place == None:
                self.inventory[key] = item


class Enemy:
    def __init__(self, name: str, hp: int, offense: int, defense: int):
        self.name = name
        self.hp = hp
        self.offense = offense
        self.defense = defense

    def attack(self, target: Player):
        if target.armor:
            target.armor.endurance -= self.offense / 2
            damage = target.armor.defense - self.offense
            if damage > 0:
                target.hp -= damage


def menu():
    print("1. Атаковать")
    print("2. Использовать навык")
    print("3. Посмотреть инвентарь")
    print("4. Сбежать")


def create_enemy(level, names):
    return Enemy(random.choice(names), 100 + 10 * random.randint(0, level), 5 + 10 * random.randint(0, level), 5 + 10 * random.randint(0, level))


enemies_names = [
    "1",
    "2",
    "3"
]

armor_names = [
    "1",
    "2",
    "3"
]

weapon_names = [
    "1",
    "2",
    "3"
]

player = Player("Hero", 100, 30)
enemy = create_enemy(player.level, enemies_names)
while True:
    print(f"Этаж {player.level}")
    print(f"ХП: {player.hp}")
    print(f"Оружие: {player.weapon}")
    print(f"Броня: {player.armor}")
    menu()
    ch = int(input("-> "))
    if ch == 1:
        player.attack(enemy)
        enemy.attack(player)
        print(enemy.hp)
        if enemy.hp <= 0:
            player.level += 1
            enemy = create_enemy(player.level, enemies_names)
            chance = random.randint(1, 100)
            if chance > 50:
                armor = Armor(random.choice(armor_names), 10 +
                              10 * random.randint(0, player.level), 100 +
                              10 * random.randint(0, player.level))
                weapon = Weapon(random.choice(weapon_names), 20 +
                                10 * random.randint(0, player.level))
                print("Вам повезло! 1 - Надеть. 2 - Добавить в инвентарь. 3 - Выбросить")
                print(f"{armor.name}: d:{armor.defense} - e:{armor.endurance}")
                ch = int(input("-> "))
                if ch == 1:
                    player.change_armor(armor)
                elif ch == 2:
                    player.add_to_inventory(armor)
                print("Вам повезло! 1 - Надеть. 2 - Добавить в инвентарь. 3 - Выбросить")
                print(f"{weapon.name}: a:{weapon.offense}")
                ch = int(input("-> "))
                if ch == 1:
                    player.change_weapon(weapon)
                elif ch == 2:
                    player.add_to_inventory(weapon)
