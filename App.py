import random

# Player creation
player_character = input("Enter your Name: ")
player_character = player_character.title()

# Player Stats
player_hp = 10 # Player health
player_attk = 1 # Player attack power
player_armor = 0 # Player over health

# All powerful dice (RNJESUS)
dice_d21 = random.randint(1, 21)

# Search object
search = dice_d21

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
        player_action = input("Action- Search, Move, or Leave: ")
        player_action = player_action.capitalize().strip()

        # Game state
        match player_action:

            # user actions
            case "Search":
                print(f"{player_character} used '{player_action}'")

                # Search functions
                if 8 <= search < 15:
                    print(f"{player_character} has found an item found")

                elif search >= 15:
                    print(f"{player_character} has found a rare item found...")

                else:
                    print(f"{player_character} has found nothing...")

            case "Move":
                print(f"{player_character} used '{player_action}'")

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