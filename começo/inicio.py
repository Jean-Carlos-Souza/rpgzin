from random import randint
from time import sleep
list_npcs = []

player = {
    'name': 'Jean',
    'level': 1,
    'damage': 25,
    'hp': 100,
    'hp_max': 100,
    'exp': 0,
    'exp_max': 30,
}

def create_npcs(level):
    new_npc = {
        'name': f'Monster #{level}',
        'level': level,
        'damage': 10 * level,
        'hp': 100 * level,
        'hp_max': 80 * level,
        'exp': 6 * level,
    }
    return new_npc

def reset_player():
    player['hp'] = player['hp_max']

def reset_npc(npc):
    npc['hp'] = npc['hp_max']

def level_up():
    if player['exp'] == player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] *= player['level']
        player['hp_max'] += 20
        player['damage'] += 25
        display_player()
    
def display_npcs():
    for npc in list_npcs:
        display_npc(npc)

def display_player():
    print(f'Name: {player['name']}  // Level: {player['level']}  // Damage: {player['damage']}  // HP: {player['hp']}/{player['hp_max']} // EXP: {player['exp']}/{player['exp_max']}') 

def display_npc(npc):
    print(f'Name: {npc['name']}  // Level: {npc['level']}  // Damage: {npc['damage']}  // HP: {npc['hp']} // EXP: {npc['exp']}') 

def to_generete_npcs(n_npcs):
    for x in range(n_npcs):
        new_npc = create_npcs(x + 1)
        list_npcs.append(new_npc)


def run_battle(npc):
    while player['hp'] > 0 and npc['hp'] > 0:
        attack_player(npc)
        attack_npc(npc)
        exi_inf_bat(npc)     
        sleep(1) 
    condi(npc)

def condi(npc):
    if player['hp'] > 0:
        print('-=' * 15)
        print(f'O {player['name']} venceu e ganhou {npc['exp']} Exp')
        print('-=' * 15)
        player['exp'] += npc['exp']
        display_player()
    else:
        print(f'O {npc['name']} venceu a batalha! Boa sorte na próxima.')
        display_npc
    
    level_up()
    reset_player()
    reset_npc(npc)

def attack_npc(npc):
    npc['hp'] -= player['damage']

def attack_player(npc):
    player['hp'] -= npc['damage']


def exi_inf_bat(npc):
    print('-' * 30, '\n')
    print(f'Player: {player["hp"]}/{player["hp_max"]}')
    print(f'{npc['name']}: {npc['hp']}/{npc['hp_max']}')

to_generete_npcs(5)
select_npc = list_npcs[0]

while True:

    run_battle(select_npc)

    print('-' * 30)
    while True:
        resp = str(input('Quer Continuar: s/n: ')).strip().lower()
        if resp in 'sn':
            break
    if resp == 'n':
        break


