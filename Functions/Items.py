import random
import json


FILEPATH = "DataFiles/items.json"

with open(FILEPATH, "r") as file:
    item_context = file.read()

data = json.loads(item_context)

common_item = data[0]
rare_item = data[1]

def get_find_items(search_arg):
    if 5 <= search_arg <= 16:
        local_item_searched = random.choice(common_item["items"])
        return local_item_searched

    elif search_arg > 16:
        local_item_searched = random.choice(rare_item["items"])
        return local_item_searched

    else:
        print(f"You have found nothing...")
        return "Nothing"

if __name__ == "__main__":
    print(common_item)
    print(rare_item)