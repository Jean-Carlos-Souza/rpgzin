from random import randint

list_npcs = []


def create_npcs():
    level = randint(0,50)
    new_npc = {
        'name': f'Monster #{level}',
        'level': level,
        'damage': 3 * level,
        'hp': 50 * level
    }
    return new_npc


    
def display_npcs():
    for npc in list_npcs:
        print(f'Name: {npc['name']}  // Level: {npc['level']}  // Damage: {npc['damage']}  // HP: {npc['hp']}')

def to_generete_npcs(n_npcs):

    for x in range(n_npcs):
        new_npc = create_npcs()
        list_npcs.append(new_npc)


to_generete_npcs(5)
display_npcs()