import random

# Player creation
player_character = input("Enter your Name: ")
player_character = player_character.title()

# Player Stats
class PlayerStats:
    player_hp = 10 # Player healths.
    player_attk = 1 # Player attack power.
    player_armor = 0 # Player over health.
    player_inventory = []

# Search object
searchable_items_common = ["Ring", "Armor Piece", "Wooden Sword", "Hp Potion"]
searchable_items_rare = ["Lucky Ring", "Knights armor", "Steel Sword", "Greater Hp Potion"]

# Item object
# TODO: Create Item object.

# Dungeon init
dungeon = False

dungeon_enter = input("Enter the dungeon: Yes or No? ")

dungeon_enter = dungeon_enter.lower().strip()

if dungeon_enter == "yes":

    dungeon = True

    print(f"{player_character} has entered the dungeon...")

    # dungeon entry
    while dungeon:

        # All powerful dice object (RN_JESUS)
        # TODO: Turn Dice class into function.
        class Dice:
            dice_d21 = random.randint(1, 21)
            dice_d6 = random.randint(1, 6)
            dice_d4 = random.randint(1, 4)

        # Player decision
        player_action = input("Action- Search, Move, Inventory, Stats, or Leave: ")
        player_action = player_action.capitalize().strip()

        search = Dice.dice_d21 # Chance of obtaining item.

        # Game state
        match player_action:

            # user actions
            case "Search" | "S":
                print(f"{player_character} used '{player_action}'")

                # Search functions
                if 5 <= search <= 16:
                    print(f"{player_character} has found an item found")
                    item_searched = random.choice(searchable_items_common)
                    PlayerStats.player_inventory.append(item_searched)
                    print(f"{item_searched} added to {player_character}s' inventory")


                elif search > 16:
                    print(f"{player_character} has found a rare item found...")
                    item_searched = random.choice(searchable_items_rare)
                    PlayerStats.player_inventory.append(item_searched)
                    print(f"{item_searched} added to {player_character}s' inventory")

                else:
                    print(f"{player_character} has found nothing...")

            case "Move" | "M":
                print(f"{player_character} used '{player_action}'")

            # Check player inventory function
            case "Inventory" | "I":
                print(f"{player_character} used '{player_action}'")

                if len(PlayerStats.player_inventory) == 0:
                    print(f"{player_character}s' inventory is empty")

                else:
                    print(f"{player_character}s' inventory")
                    for index, item in enumerate(PlayerStats.player_inventory):
                        index = index + 1
                        print(f"{index}: {item}")

            # Check player stats function
            case "Stats" | "St":
                print(f"{player_character} used '{player_action}'")
                print(f"{player_character}s' HP: {PlayerStats.player_hp}")
                print(f"{player_character}s' ARMOR: {PlayerStats.player_armor}")
                print(f"{player_character}s' ATTK: {PlayerStats.player_attk}")

            case "Leave" | "L":
                print(f"{player_character} used '{player_action}'")
                dungeon = False

            case _:
                print("Unknown action !...")

# Exit dungeon
elif dungeon_enter == "no":
    print("Coward...")

else:
    print("Unknown action !...")

print("Exited...")