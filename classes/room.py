import copy

class Room:
    def __init__(self, name, dict_monsters={}, picture_url=""):
        self.name = name
        self.dict_monsters = dict_monsters
        self.picture_url = picture_url

    def add_monster(self, monster):
        self.dict_monsters[monster.name] = monster
    
    def remove_monster(self, monster_name):
        self.dict_monsters.pop(monster_name)

    