from items import shop
from quests import side_quest, talk_to_keeper
from skills import train


def talk(player, tile):
    if tile == "E":
        talk_to_keeper(player)
    elif tile == "H":
        side_quest(player, "rat_quest", "Rat Tail", 6, 4,
                   "Nia: The rats got into my medicine. Bring me one Rat Tail from the mine.")
    elif tile == "T":
        print("Tess: A spell is worth learning before you need it. Pick a lesson.")
        train(player)
    elif tile == "S":
        side_quest(player, "bat_quest", "Bat Wing", 8, 5,
                   "Bram: I'm repairing the bellows. Bring me one Bat Wing for a patch.")
    elif tile == "M":
        print("Mira: Heading below? I have two sizes of healing potion.")
        shop(player)
    else:
        print("Stand on E, H, T, S, or M and press e to talk.")
