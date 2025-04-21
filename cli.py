import Functions.Items as Item
import Functions.Dice as Dice


# Player Stats
# TODO: Create function for player stats and storing player inventory.
class PlayerStats:
    player_hp = 10 # Player healths.
    player_attk = 1 # Player attack power.
    player_armor = 0 # Player over health.
    player_inventory = []


# Item object
# TODO: Create Item object.


# Player creation
player_character = input("Enter your Name: ")
player_character = player_character.title()

# Dungeon init
dungeon = False

dungeon_enter = input("Enter the dungeon: Yes or No? ")

dungeon_enter = dungeon_enter.lower().strip()

if dungeon_enter == "yes":

    dungeon = True

    print(f"{player_character} has entered the dungeon...")

    # dungeon entry
    while dungeon:

        search_item = Dice.get_dice_type("dice_d21")  # Chance of obtaining item.

        # Player decision
        player_action = input("Action- Search, Move, Inventory, Stats, or Leave: ")
        player_action = player_action.capitalize().strip()

        # Game state
        match player_action:

            # user actions
            case "Search" | "S":
                print(f"{player_character} used '{player_action}'")

                item_searched = Item.get_find_items(search_item)

                PlayerStats.player_inventory.append(item_searched)

                print(f"{item_searched} added to {player_character}s' inventory")


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