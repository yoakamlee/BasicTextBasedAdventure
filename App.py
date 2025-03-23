player_character = input("Enter your Name: ")
player_character = player_character.title()

print(player_character)

dungeon = False

dungeon_enter = input("Enter the dungeon: Yes or No? ")

dungeon_enter = dungeon_enter.lower().strip()

if dungeon_enter == "yes":
    dungeon = True

    while dungeon:
        print("You have entered the dungeon...")
        break

elif dungeon_enter == "no":
    print("Cowards...")

else:
    breakpoint()

print("Exited...")