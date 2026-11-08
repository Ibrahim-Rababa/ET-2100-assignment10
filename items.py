HEALING = {"Potion": 12, "Large Potion": 22}
PRICES = {"Potion": 5, "Large Potion": 9}


def add_item(player, name):
    bag = player["inventory"]
    bag[name] = bag.get(name, 0) + 1


def remove_item(player, name):
    bag = player["inventory"]
    bag[name] -= 1
    if bag[name] == 0:
        del bag[name]


def show_bag(player):
    print("INVENTORY")
    if not player["inventory"]:
        print("Empty")
    for name, amount in player["inventory"].items():
        print(f"{name} x{amount}")


def choose_potion():
    choice = input("[1] Potion (+12 HP)  [2] Large Potion (+22 HP)  [0] Back: ").strip()
    if choice == "1":
        return "Potion"
    if choice == "2":
        return "Large Potion"
    if choice != "0":
        print("Enter 1, 2, or 0.")
    return None


def drink(player):
    name = choose_potion()
    if name is None:
        return False
    if name not in player["inventory"]:
        print("You don't have that potion.")
        return False
    if player["hp"] == player["max_hp"]:
        print("Your HP is already full.")
        return False
    old_hp = player["hp"]
    player["hp"] = min(player["max_hp"], old_hp + HEALING[name])
    remove_item(player, name)
    print(f"Recovered {player['hp'] - old_hp} HP.")
    return True


def shop(player):
    print(f"Gold: {player['gold']} | Potion: 5 gold | Large Potion: 9 gold")
    name = choose_potion()
    if name is None:
        return
    if player["gold"] < PRICES[name]:
        print("You need more gold.")
        return
    player["gold"] -= PRICES[name]
    add_item(player, name)
    print(f"Bought {name}. Gold left: {player['gold']}.")
