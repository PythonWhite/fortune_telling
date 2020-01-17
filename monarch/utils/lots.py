import random


def gen_numbers(lots: list):
    lengths = len(lots)
    if lengths == 0:
        return None
    lot_dict = {i: v for i, v in enumerate(lots)}
    index = random.randint(0, lengths)
    return lot_dict[index]
