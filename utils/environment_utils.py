from copy import copy
from classes.Environment import Environment



def monster_join_battle(custom_name, monster_name, env):
    monster = copy(env.dict_monsters[monster_name])
    monster.name = custom_name
    env.add_monster(monster)