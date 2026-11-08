from colorama import Fore, Style


def new_player():
    return {
        "level": 1,
        "xp": 0,
        "hp": 32,
        "max_hp": 32,
        "gold": 10,
        "map": "Harbor",
        "x": 1,
        "y": 1,
        "inventory": {"Potion": 2},
        "skills": [],
        "main_step": 0,
        "rat_quest": "new",
        "bat_quest": "new",
        "defeated": [],
    }


def attack_power(player):
    return 5 + player["level"]


def gain_xp(player, amount):
    player["xp"] += amount
    while player["xp"] >= 10 * player["level"]:
        player["xp"] -= 10 * player["level"]
        player["level"] += 1
        player["max_hp"] += 6
        player["hp"] = player["max_hp"]
        print(Fore.GREEN + f"Level up! Level {player['level']}. HP restored." + Style.RESET_ALL)


def show_status(player):
    print(Fore.CYAN + "CHARACTER" + Style.RESET_ALL)
    print(f"Level {player['level']} | XP {player['xp']}/{10 * player['level']}")
    print(f"HP {player['hp']}/{player['max_hp']} | Attack {attack_power(player)} | Gold {player['gold']}")
    print(f"Location: {player['map']} ({player['x']}, {player['y']})")
    print("Skills:", ", ".join(player["skills"]) or "None yet")
