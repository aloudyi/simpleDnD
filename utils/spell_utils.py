from classes.Spell import Spell
from copy import copy

# Spell Management
def create_spell(spellname, env):
    new_spell = Spell(name=spellname)
    env.add_spell(new_spell)
def link_spell(entity, spellname, target_dict):
    spell = target_dict[spellname]
    entity.spells[spellname] = copy(spell)
def set_spell_success(message, spellname, target_dict):
    msg = message.content
    success_condition = msg.split("set spell success ", 1)[1]
    target_dict[spellname].success_condition = int(success_condition)
def set_spell_type(message, spellname, target_dict):
    msg = message.content
    type = msg.split("set spell type ", 1)[1]
    target_dict[spellname].type = type
def set_spell_current_cooldown(message, spellname, target_dict):
    msg = message.content
    current_cooldown = msg.split("set spell current_cooldown ", 1)[1]
    target_dict[spellname].current_cooldown = int(current_cooldown)
def set_spell_crit(message, spellname, target_dict):
    msg = message.content
    crit_condition = msg.split("set spell crit ", 1)[1]
    target_dict[spellname].crit_condition = int(crit_condition)
def set_spell_damage(message, spellname, target_dict):
    msg = message.content
    damage = msg.split("set spell damage ", 1)[1]
    target_dict[spellname].damage = int(damage)
def set_spell_heal(message, spellname, target_dict):
    msg = message.content
    heal = msg.split("set spell heal ", 1)[1]
    target_dict[spellname].heal = int(heal)
def set_spell_cooldown(message, spellname, target_dict):
    msg = message.content
    cooldown = msg.split("set spell cooldown ", 1)[1]
    target_dict[spellname].cooldown = int(cooldown)
def set_spell_effect(message, spellname, target_dict):
    msg = message.content
    effect = msg.split("set spell effect ", 1)[1]
    target_dict[spellname].effect = effect
def set_spell_targets(message, spellname, target_dict):
    msg = message.content
    targets = msg.split("set spell targets ", 1)[1]
    target_dict[spellname].targets = int(targets)
def set_spell_description(message, spellname, target_dict):
    msg = message.content
    description = msg.split("set spell description ", 1)[1]
    target_dict[spellname].description = description
def set_spell_picture(message, spellname, target_dict):
    msg = message.content
    picture_url = msg.split("set spell picture ", 1)[1]
    target_dict[spellname].picture_url = picture_url
def set_spell_crit_effect(message, spellname, target_dict):
    msg = message.content
    crit_effect = msg.split("set spell crit_effect ", 1)[1]
    target_dict[spellname].crit_effect = crit_effect
def set_spell_crit_effect_duration(message, spellname, target_dict):
    msg = message.content
    crit_effect_duration = msg.split("set spell crit_effect_duration ", 1)[1]
    target_dict[spellname].crit_effect_duration = int(crit_effect_duration)
def set_spell_crit_damage(message, spellname, target_dict):
    msg = message.content
    crit_damage = msg.split("set spell crit_damage ", 1)[1]
    target_dict[spellname].crit_damage = int(crit_damage)
def set_spell_crit_heal(message, spellname, target_dict):
    msg = message.content
    crit_heal = msg.split("set spell crit_heal ", 1)[1]
    target_dict[spellname].crit_heal = int(crit_heal)
def set_spell_effect_duration(message, spellname, target_dict):
    msg = message.content
    effect_duration = msg.split("set spell effect_duration ", 1)[1]
    print(effect_duration)
    target_dict[spellname].effect_duration = int(effect_duration)
def set_spell_modifier(message, spellname, target_dict):
    msg = message.content
    modifier = msg.split("set spell modifier ", 1)[1]
    target_dict[spellname].add_modifier = int(modifier)
def remove_spell(message, target_dict):
    content = message.content.split("remove spell ", 1)[1]
    content = content.split(" ")
    spellname = content[0]
    target_dict.pop(spellname)
