import json


# Player Stats
FILEPATH_Test = "../DataFiles/player_stats.json"
FILEPATH = "DataFiles/player_stats.json"

with open(FILEPATH, "r") as file:
    content = file.read()

data = json.loads(content)

player_data = data[0]

class PlayerStats:
    player_hp = player_data["player_hp"] # Player healths.
    player_attk = player_data["player_attk"] # Player attack power.
    player_armor = player_data["player_armor"] # Player over health.
    player_inventory = player_data["player_inventory"]

# TODO: Adding to player inventory

if __name__ == "__main__":
    print(player_data)
