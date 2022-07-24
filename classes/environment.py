import pickle as pkl
from copy import copy
import json

class Environment:
    def __init__(self,
                 dict_characters={},
                 dict_monsters={},
                 dict_spells={},
                 dict_battle={},
                 dict_dungeons={},
                 dict_current_dungeon={},
                 current_room_name="blank"):
        self.dict_monsters = dict_monsters  # Monster Library
        self.dict_characters = dict_characters  # Character Library
        self.dict_spells = dict_spells  # Spell Library
        self.dict_battle = dict_battle  # Monsters in battle
        self.dict_dungeons = dict_dungeons
        self.dict_current_dungeon = dict_current_dungeon
        self.current_room_name = current_room_name
        
    def use_spell(self, caster, spellname, target, env):
        spells = env.dict_spells
        spell = spells[spellname]
        msg_append = ""
        for spellkey in spells.keys(): 
            if(spells[spellkey].current_cooldown!=0):
                spells[spellkey].current_cooldown-=1

        dice_roll, modifier, message = target.apply_spell(spell,caster)
        if (target.name in self.dict_battle.keys()):
            if (target.current_hp == 0):
                env.dict_battle.pop(target.name)
                msg_append = "\n**" + caster.name + " defeated " + target.name + "**."
        # Reduce character spells cooldown
        for spellkey in caster.spells.keys():
            if(caster.spells[spellkey]!=0):
                print(caster.spells[spellkey])
                caster.spells[spellkey] -= 1
        # Set used spell cooldown on max.
        caster.spells[spellname] = spell.cooldown

        out_msg = "**" + caster.name + "** used `" + spellname + "` on **" + target.name + "**." + msg_append
        return out_msg, dice_roll, modifier, message


    def get_monster(self, monster_name):
        return copy(self.dict_monsters[monster_name])

    def add_monster(self, monster):
        self.dict_battle[monster.name] = monster

    def add_character(self, character):
        self.dict_characters[character.user_id] = character

    def add_spell(self, spell):
        self.dict_spells[spell.name] = spell

    def create_monster(self, monster):
        self.dict_monsters[monster.name] = monster

    def add_dungeon(self, dungeon):
        self.dict_dungeons[dungeon.name] = dungeon

    def set_battle_name(self,name):
        self.dict_battle["name"]=name
    
    def load_dungeon(self, dungeon_name):
        dungeon = self.dict_dungeons[dungeon_name]
        self.dict_current_dungeon = copy(dungeon)
    
    def load_room(self, room_name):
        room = self.dict_current_dungeon.dict_rooms[room_name]
        self.current_room_name = room.name
        monsters = room.dict_monsters
        print(room.dict_monsters)
        print(monsters.keys())
        for monster_name in monsters.keys():
            self.dict_battle[monster_name] = copy(monsters[monster_name])

        
    def save_env(self,path_to_save):
        save = {
            "monsters": self.dict_monsters,
            "characters": self.dict_characters,
            "spells": self.dict_spells,
            "battle": self.dict_battle,
            "dungeons":self.dict_dungeons,
            "current_dungeon":self.dict_current_dungeon,
            "current_room_name":self.current_room_name
        }

        output = open(path_to_save, "wb")
        pkl.dump(save, output)
        output.close()

    def reload_env(self,path_to_save):
        input = open(path_to_save, "rb")
        save = pkl.load(input)
        self.dict_characters = save["characters"]
        self.dict_monsters = save["monsters"]
        self.dict_spells = save["spells"]
        self.dict_battle = save["battle"]
        self.dict_dungeons = save["dungeons"]
        self.dict_current_dungeon =save["current_dungeon"]
        self.current_room_name = save["current_room_name"]
        input.close()