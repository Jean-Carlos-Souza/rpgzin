from random import randint

list_npcs = []


def create_monster():
    level = randint(0,50)
    new_npc = {
        'name': f'Monster #{level}',
        'level': level,
        'damage': 3 * level,
        'hp': 50 * level
    }
    list_npcs.append(new_npc)

    print(list_npcs)

create_monster()