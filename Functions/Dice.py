import random


# All powerful dice object (RN_JESUS)
def get_dice(dice_arg):
    if dice_arg == "dice_d21":
        dice_d21 = random.randint(1, 21)
        return dice_d21

    elif dice_arg == "dice_d6":
        dice_d6 = random.randint(1, 6)
        return dice_d6

    elif dice_arg == "dice_d4":
        dice_d4 = random.randint(1, 4)
        return dice_d4

def get_dice_type(dice_arg):
    local_dice = get_dice(dice_arg)
    return local_dice
