from numpy import maximum, minimum
from numpy.random import randint

class Entity:
    def __init__(self,name,race,max_hp=10,current_hp=10,state_duration=0,
                 spells={},state="normal", modifier=0,description="",picture_url=""):
        self.name = name
        self.race = race
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.spells = spells
        self.state = state
        self.state_duration = state_duration
        self.modifier = modifier
        self.description = description
        self.picture_url = picture_url

    def damage(self, damage):
        self.current_hp = int(maximum(0, self.current_hp - damage))
        if (self.current_hp == 0):
            self.state = "unanimated"

    def heal(self, heal):
        if (self.current_hp == 0):
            self.state = "normal"
        self.current_hp = int(minimum(self.max_hp, self.current_hp + heal))

    def apply_spell(self, spell, caster):
        dice_roll = int(randint(1, 21)) + self.modifier
        modifier = self.modifier
        self.modifier = 0
        message = "blank"
        if (spell.type == "normal"):
            if (dice_roll >= spell.crit_condition):
                add_heal = spell.crit_heal
                add_damage = spell.crit_damage
                add_duration = spell.crit_effect_duration
            else:
                add_heal = 0
                add_damage = 0
                add_duration = 0
            
            if (dice_roll >= spell.success_condition):
                if(spell.effect=="sustain" or spell.crit_effect =="sustain"):
                    caster.heal(spell.heal+add_heal)
                if (spell.effect == "heal" or spell.crit_effect == "heal"):
                    self.heal(spell.heal + add_heal)
                elif (spell.effect == "buff"):
                    self.modifier = spell.add_modifier
                elif (spell.effect == "drain"):
                    self.heal(spell.heal + add_heal)
                    self.damage(spell.damage + add_damage)
                    
                self.damage(spell.damage + add_damage)
                if (spell.effect == "stun" or spell.crit_effect == "stun"):
                    self.state = "stunned"
                    self.state_duration = spell.effect_duration + add_duration
                if(spell.effect == "alarm" or spell.crit_effect == "alarm"):
                    message = "INTRUDEEERS, £EZZ$az!!?@£FZ%Qµ$$zEZ$az!!?@!!!"
        # Adil's bullshit spells
        elif (spell.type == "double-edge"):
            if (dice_roll < spell.success_condition):
                if (spell.effect == "heal"):
                    self.damage(spell.damage)
                else:
                    self.heal(spell.heal)
            else:
                if (spell.effect == "heal"):
                    self.heal(spell.heal)
                else:
                    self.damage(spell.damage)
        return dice_roll, modifier, message