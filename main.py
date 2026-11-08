from json import JSONDecodeError
from pathlib import Path

from colorama import Fore, Style, just_fix_windows_console
from tinydb import TinyDB

from accounts import authenticate, save_game
from items import drink, show_bag
from maps import DIRECTIONS, current_tile, draw_map, move
from npcs import talk
from player import show_status
from quests import show_quests


def play(accounts, account):
    player = account["progress"]
    if player["main_step"] == 4:
        print("Welcome back, champion. Your victory is saved.")
        show_status(player)
        show_bag(player)
        show_quests(player)
        return
    while True:
        draw_map(player)
        print("w/a/s/d move | e talk | c character | i inventory | p drink | j journal | q save and quit")
        command = input("Your move: ").strip().lower()
        if command == "q":
            save_game(accounts, account.doc_id, player)
            print("Game saved. Goodbye!")
            return
        if command in DIRECTIONS:
            move(player, command)
        elif command == "e":
            talk(player, current_tile(player))
        elif command == "c":
            show_status(player)
        elif command == "i":
            show_bag(player)
        elif command == "p":
            drink(player)
        elif command == "j":
            show_quests(player)
        else:
            print("Unknown command. Use a key from the menu.")
            continue

        save_game(accounts, account.doc_id, player)
        if player["main_step"] == 4:
            print("Victory saved. Final character sheet:")
            show_status(player)
            return


def main():
    just_fix_windows_console()
    print(Fore.CYAN + "BEACON BELOW" + Style.RESET_ALL)
    print("Fog covers the harbor. Without its beacon, the next ship will strike the rocks.")
    print("Keeper Ada waits above the flooded mine. Stand on E and press e to hear her plan.")
    path = Path(__file__).with_name("rpg_save.json")
    try:
        with TinyDB(path) as db:
            accounts = db.table("accounts")
            account = authenticate(accounts)
            if account is not None:
                play(accounts, account)
    except (EOFError, KeyboardInterrupt):
        print("\nGame closed. Log in again to resume from the last completed map command.")
    except (OSError, JSONDecodeError) as error:
        print(f"Could not read or write the save file: {error}")
        print("Check the project folder and keep a backup of rpg_save.json.")


if __name__ == "__main__":
    main()
