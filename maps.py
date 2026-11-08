from colorama import Fore, Style

from battle import fight
from monsters import ENEMIES


MAPS = {
    "Harbor": [
        "#############",
        "#E.H.T.S.M.>#",
        "#..##.##.#..#",
        "#.....#.....#",
        "#############",
    ],
    "Mine": [
        "###########",
        "#<r.b.g...#",
        "#########.#",
        "#F..v.k...#",
        "###########",
    ],
}

DIRECTIONS = {"w": (0, -1), "a": (-1, 0), "s": (0, 1), "d": (1, 0)}


def current_tile(player):
    return MAPS[player["map"]][player["y"]][player["x"]]


def draw_map(player):
    print(f"\n{player['map']} | HP {player['hp']}/{player['max_hp']} | Gold {player['gold']}")
    for y, row in enumerate(MAPS[player["map"]]):
        line = ""
        for x, tile in enumerate(row):
            if x == player["x"] and y == player["y"]:
                line += Fore.CYAN + "@" + Style.RESET_ALL
            elif tile in player["defeated"]:
                line += "."
            elif tile in ENEMIES:
                line += Fore.RED + tile + Style.RESET_ALL
            elif tile in "EHTSM":
                line += Fore.YELLOW + tile + Style.RESET_ALL
            else:
                line += tile
        print(line)
    print("@ you | # wall | . path | > mine | < harbor")
    if player["map"] == "Harbor":
        print("E Ada | H Nia | T Tess | S Bram | M Mira")
    else:
        print("r rat | b bat | g goblin | k golem | v wolf | F king")


def move(player, direction):
    dx, dy = DIRECTIONS[direction]
    x = player["x"] + dx
    y = player["y"] + dy
    # Every map has a solid outer wall, so you can never step beyond its edges.
    tile = MAPS[player["map"]][y][x]
    if tile == "#":
        print("A wall blocks that direction.")
        return
    if tile == ">" and player["main_step"] == 0:
        print("Speak to Ada (E) before entering the mine.")
        return
    if tile == "F" and player["main_step"] < 3:
        print("The king's seal is closed. Check your journal with j.")
        return

    player["x"] = x
    player["y"] = y
    if tile == ">":
        player["map"] = "Mine"
        player["x"] = 1
        player["y"] = 1
    elif tile == "<":
        player["map"] = "Harbor"
        player["x"] = 11
        player["y"] = 1
    elif tile in ENEMIES and tile not in player["defeated"]:
        fight(player, tile)
