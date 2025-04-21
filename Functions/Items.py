import random

FILEPATH_Common = "DataFiles/Items_common.txt"
FILEPATH_rare = "DataFiles/Items_rare.txt"


def get_find_items(search_arg, filepath_common=FILEPATH_Common, filepath_rare=FILEPATH_rare):
    if 5 <= search_arg <= 16:
        with open(filepath_common, "r") as local_file:
            data = local_file.readlines()
            data = [local_item.strip("\n") for local_item in data]
            local_item_searched = random.choice(data)
            return local_item_searched

    elif search_arg > 16:
        with open(filepath_rare, "r") as local_file:
            data = local_file.readlines()
            data = [local_item.strip("\n") for local_item in data]
            local_item_searched = random.choice(data)
            return local_item_searched

    else:
        print(f"You have found nothing...")
