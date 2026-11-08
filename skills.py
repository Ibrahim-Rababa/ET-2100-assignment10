class Skill:
    # A cooldown of 2 skips the next two turns.
    def next_ready_turn(self, turn):
        return turn + self.cooldown + 1


class Fireball(Skill):
    name = "Fireball"
    level = 1
    cooldown = 2

    def use(self, player, enemy):
        damage = 10 + 2 * player["level"]
        enemy.take_damage(damage)
        print(f"Fireball deals {damage} damage.")
        return True


class Heal(Skill):
    name = "Heal"
    level = 2
    cooldown = 3

    def use(self, player, enemy):
        old_hp = player["hp"]
        if old_hp == player["max_hp"]:
            print("Your HP is already full.")
            return False
        player["hp"] = min(player["max_hp"], old_hp + 10 + 2 * player["level"])
        print(f"Heal restores {player['hp'] - old_hp} HP.")
        return True


SPELLS = {"2": Fireball(), "3": Heal()}


def train(player):
    print("Free lessons: [2] Fireball (level 1)  [3] Heal (level 2)  [0] Back")
    choice = input("Learn which skill? ").strip()
    if choice == "0":
        return
    if choice not in SPELLS:
        print("Enter 2, 3, or 0.")
        return
    skill = SPELLS[choice]
    if skill.name in player["skills"]:
        print("You already know that skill.")
    elif player["level"] < skill.level:
        print(f"Come back at level {skill.level}.")
    else:
        player["skills"].append(skill.name)
        print(f"Learned {skill.name}!")
