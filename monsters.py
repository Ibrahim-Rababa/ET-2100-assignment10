class Monster:
    # Subclasses supply the starting stats. Each enemy gets its own current HP.
    def __init__(self):
        self.hp = self.max_hp

    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)


class TunnelRat(Monster):
    name = "Tunnel Rat"
    max_hp = 10
    damage = 3
    xp = 4
    gold = 3
    item = "Rat Tail"


class AshBat(Monster):
    name = "Ash Bat"
    max_hp = 12
    damage = 3
    xp = 6
    gold = 4
    item = "Bat Wing"


class Goblin(Monster):
    name = "Goblin"
    max_hp = 16
    damage = 4
    xp = 7
    gold = 5
    item = "Potion"


class StoneGolem(Monster):
    name = "Stone Golem"
    max_hp = 24
    damage = 5
    xp = 10
    gold = 8
    item = "Beacon Lens"


class CaveWolf(Monster):
    name = "Cave Wolf"
    max_hp = 20
    damage = 5
    xp = 8
    gold = 6
    item = "Potion"


class HollowKing(Monster):
    name = "Hollow King"
    max_hp = 38
    damage = 6
    xp = 15
    gold = 20
    item = "Large Potion"


# Each enemy symbol occurs once, so it also identifies a cleared encounter.
ENEMIES = {"r": TunnelRat, "b": AshBat, "g": Goblin, "k": StoneGolem, "v": CaveWolf, "F": HollowKing}
