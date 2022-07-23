import pickle as pkl

class Environment:
    def __init__(self,
                 dict_characters={},
                 dict_monsters={},
                 dict_spells={},
                 dict_battle={}):
        self.dict_monsters = dict_monsters  # Monster Library
        self.dict_characters = dict_characters  # Character Library
        self.dict_spells = dict_spells  # Spell Library
        self.dict_battle = dict_battle  # Monsters in battle

    def use_spell(self, caster, spellname, target, env):
        spells = caster.spells
        spell = spells[spellname]
        msg_append = ""
        for spellkey in spells.keys(): 
            if(spells[spellkey].current_cooldown!=0):
                spells[spellkey].current_cooldown-=1
        if (target.name in self.dict_battle.keys()):
            if (target.current_hp == 0):
                env.dict_battle.pop(target.name)
                msg_append = "\n**" + caster.name + " defeated " + target.name + "**."

        dice_roll, modifier = target.apply_spell(spell,caster)
        
        # Reduce character spells cooldown
        for spellkey in caster.spells.keys():
            if(caster.spells[spellkey].current_cooldown!=0):
                caster.spells[spellkey].current_cooldown -= 1
        # Set used spell cooldown on max.
        caster.spells[spellname].current_cooldown = caster.spells[spellname].cooldown

        out_msg = "**" + caster.name + "** used `" + spellname + "` on **" + target.name + "**." + msg_append
        return out_msg, dice_roll, modifier

    def add_monster(self, monster):
        self.dict_battle[monster.name] = monster

    def add_character(self, character):
        self.dict_characters[character.user_id] = character

    def add_spell(self, spell):
        self.dict_spells[spell.name] = spell

    def create_monster(self, monster):
        self.dict_monsters[monster.name] = monster

    def save_env(self,path_to_current):
        save = {
            "monsters": self.dict_monsters,
            "characters": self.dict_characters,
            "spells": self.dict_spells,
            "battle": self.dict_battle
        }
        output = open(path_to_current, "wb")
        pkl.dump(save, output)
        output.close()
        print("Saved env !")

    def reload_env(self,path_to_current):
        input = open(path_to_current, "rb")
        save = pkl.load(input)
        self.dict_characters = save["characters"]
        self.dict_monsters = save["monsters"]
        self.dict_spells = save["spells"]
        self.dict_battle = save["battle"]
        input.close()