
# Player creation
player_character = input("Enter your Name: ")
player_character = player_character.title()

# Player Stats
# Player health
player_hp = 10
# Player attack power
player_attk = 1
# Player over health
player_armor = 0

print(player_character)

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

            case "Move":
                print(f"{player_character} used '{player_action}'")

            case "Leave":
                print(f"{player_character} used '{player_action}'")
                break

            case _:
                print("Unknown action !...")

# Exit dungeon
elif dungeon_enter == "no":
    print("Coward...")

else:
    print("Unknown action !...")

print("Exited...")