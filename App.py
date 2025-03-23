import random

# Player creation
player_character = input("Enter your Name: ")
player_character = player_character.title()

# Player Stats
player_hp = 10 # Player health
player_attk = 1 # Player attack power
player_armor = 0 # Player over health
player_inventory = []

# All powerful dice object (RN_JESUS)
dice_d21 = random.randint(1,21)
dice_d6 = random.randint(1,6)
dice_d4 = random.randint(1,4)

# Search object
search = dice_d21
searchable_items_common = ["Ring", "Armor Piece", "Wooden Sword", "Hp Potion"]
searchable_items_rare = ["Lucky Ring", "Knights armor", "Steel Sword", "Greater Hp Potion"]

# Dungeon init
dungeon = False

dungeon_enter = input("Enter the dungeon: Yes or No? ")

dungeon_enter = dungeon_enter.lower().strip()

if dungeon_enter == "yes":

    dungeon = True

    print(f"{player_character} has entered the dungeon...")

    # dungeon entry
    while dungeon:

        # Player decision
        player_action = input("Action- Search, Move, Inventory, or Leave: ")
        player_action = player_action.capitalize().strip()

        # Game state
        match player_action:

            # user actions
            case "Search":
                print(f"{player_character} used '{player_action}'")

                # Search functions
                if 6 <= search <= 16:
                    print(f"{player_character} has found an item found")
                    item_searched = random.choice(searchable_items_common)
                    player_inventory.append(item_searched)
                    print(f"{item_searched} added to {player_character}s' inventory")


                elif search > 16:
                    print(f"{player_character} has found a rare item found...")
                    item_searched = random.choice(searchable_items_rare)
                    player_inventory.append(item_searched)
                    print(f"{item_searched} added to {player_character}s' inventory")

                else:
                    print(f"{player_character} has found nothing...")

            case "Move":
                print(f"{player_character} used '{player_action}'")

            case "Inventory":
                if len(player_inventory) == 0:
                    print(f"{player_character}s' inventory is empty")

                else:
                    print(f"{player_character}s' inventory")
                    for item in player_inventory:
                        print(item)

            case "Leave":
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