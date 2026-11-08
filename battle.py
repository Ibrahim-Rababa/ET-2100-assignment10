from colorama import Fore, Style

from items import add_item, drink
from monsters import ENEMIES
from player import attack_power, gain_xp
from quests import after_victory
from skills import SPELLS


def fight(player, symbol):
    enemy = ENEMIES[symbol]()
    turn = 1
    ready_on = {}
    print(Fore.RED + f"A {enemy.name} blocks your path!" + Style.RESET_ALL)

    while enemy.hp > 0 and player["hp"] > 0:
        print(f"Turn {turn} | Your HP: {player['hp']}/{player['max_hp']} | {enemy.name}: {enemy.hp} HP")
        print("[1] Attack  [4] Drink potion")
        for key, skill in SPELLS.items():
            if skill.name in player["skills"]:
                wait = max(0, ready_on.get(skill.name, 1) - turn)
                if wait > 0:
                    print(f"[{key}] {skill.name} (ready in {wait} turns)")
                else:
                    print(f"[{key}] {skill.name} (ready)")
        choice = input("Battle action: ").strip()

        if choice == "1":
            damage = attack_power(player)
            enemy.take_damage(damage)
            print(f"You hit for {damage} damage.")
        elif choice == "4":
            if not drink(player):
                continue
        elif choice in SPELLS:
            skill = SPELLS[choice]
            if skill.name not in player["skills"]:
                print("Learn that skill from Tess first.")
                continue
            if turn < ready_on.get(skill.name, 1):
                print(f"{skill.name} is on cooldown until turn {ready_on[skill.name]}.")
                continue
            if not skill.use(player, enemy):
                continue
            ready_on[skill.name] = skill.next_ready_turn(turn)
        else:
            print("Choose one of the displayed battle actions.")
            continue

        if enemy.hp > 0:
            player["hp"] = max(0, player["hp"] - enemy.damage)
            print(f"{enemy.name} hits you for {enemy.damage}.")
        turn += 1

    if player["hp"] == 0:
        print("You wake up with full HP beside Ada. This enemy is still in the mine.")
        player["map"] = "Harbor"
        player["x"] = 1
        player["y"] = 1
        player["hp"] = player["max_hp"]
        return

    player["defeated"].append(symbol)
    player["gold"] += enemy.gold
    add_item(player, enemy.item)
    print(f"Victory! +{enemy.gold} gold, +{enemy.xp} XP, and a {enemy.item}.")
    gain_xp(player, enemy.xp)
    after_victory(player, symbol)
