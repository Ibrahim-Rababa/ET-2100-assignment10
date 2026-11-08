from colorama import Fore, Style

from items import remove_item
from player import gain_xp


MAIN_STEPS = [
    "Speak to Keeper Ada (E) in the harbor.",
    "Defeat the Stone Golem (k) for the Beacon Lens.",
    "Bring the Beacon Lens to Keeper Ada (E).",
    "Defeat the Hollow King (F) in the mine.",
    "The beacon is lit. Main quest complete!",
]


def show_quests(player):
    print(Fore.YELLOW + "QUEST JOURNAL" + Style.RESET_ALL)
    print("Main:", MAIN_STEPS[player["main_step"]])
    print("Rat Tail for Nia (H):", player["rat_quest"])
    print("Bat Wing for Bram (S):", player["bat_quest"])


def talk_to_keeper(player):
    step = player["main_step"]
    if step == 0:
        player["main_step"] = 1
        print("Ada: The beacon went dark. The Stone Golem has its lens. Bring it home.")
    elif step == 2:
        remove_item(player, "Beacon Lens")
        player["main_step"] = 3
        print("Ada: The lens is set! The king's seal is broken. Find him beneath the harbor.")
    else:
        print("Ada:", MAIN_STEPS[step])


def after_victory(player, symbol):
    if symbol == "k" and player["main_step"] == 1:
        player["main_step"] = 2
        print("Main quest updated: bring the lens to Ada.")
    elif symbol == "F" and player["main_step"] == 3:
        player["main_step"] = 4
        print(Fore.GREEN + "YOU WIN! The Hollow King falls. The harbor beacon shines again." + Style.RESET_ALL)


def side_quest(player, key, item, gold, xp, request):
    if player[key] == "new":
        player[key] = "active"
        print(request)
    elif player[key] == "done":
        print("Thanks again. You already earned your reward.")
    elif item in player["inventory"]:
        remove_item(player, item)
        player[key] = "done"
        player["gold"] += gold
        gain_xp(player, xp)
        print(f"Quest complete! Received {gold} gold and {xp} XP.")
    else:
        print(request)
