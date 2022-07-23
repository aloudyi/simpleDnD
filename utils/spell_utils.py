from copy import copy

# Spell Management
def create_spell(new_spell, env):
    env.add_spell(new_spell)
    out_msg = new_spell.name+" has been added to spells, if you want to see it's informations use the (**!spellbook** `spellname`) command"
    return out_msg
def link_spell(entity, spellname, target_dict):
    spell = target_dict[spellname]
    entity.spells[spellname] = copy(spell)
    out_msg = spellname+" has been linked to "
    return out_msg
def set_spell_success(message, spellname, target_dict):
    msg = message.content
    success_condition = msg.split("set spell success ", 1)[1]
    target_dict[spellname].success_condition = int(success_condition)
    out_msg = "The success condition of "+spellname+" has been set to "+success_condition+"."
    return out_msg
def set_spell_type(message, spellname, target_dict):
    msg = message.content
    type = msg.split("set spell type ", 1)[1]
    target_dict[spellname].type = type
    out_msg = "The type of "+spellname+" has been set to "+type+"."
    return out_msg
def set_spell_current_cooldown(message, spellname, target_dict):
    msg = message.content
    current_cooldown = msg.split("set spell current_cooldown ", 1)[1]
    target_dict[spellname].current_cooldown = int(current_cooldown)
    out_msg = "The current_cooldown of "+spellname+" has been set to "+current_cooldown+"."
    return out_msg
def set_spell_crit(message, spellname, target_dict):
    msg = message.content
    crit_condition = msg.split("set spell crit ", 1)[1]
    target_dict[spellname].crit_condition = int(crit_condition)
    out_msg = "The crit_condition of "+spellname+" has been set to "+crit_condition+"."
    return out_msg
def set_spell_damage(message, spellname, target_dict):
    msg = message.content
    damage = msg.split("set spell damage ", 1)[1]
    target_dict[spellname].damage = int(damage)
    out_msg = "The damage of "+spellname+" has been set to "+damage +"."
    return out_msg
def set_spell_heal(message, spellname, target_dict):
    msg = message.content
    heal = msg.split("set spell heal ", 1)[1]
    target_dict[spellname].heal = int(heal)
    out_msg = "The heal of "+spellname+" has been set to "+ heal+"."
    return out_msg
def set_spell_cooldown(message, spellname, target_dict):
    msg = message.content
    cooldown = msg.split("set spell cooldown ", 1)[1]
    target_dict[spellname].cooldown = int(cooldown)
    out_msg = "The cooldown of "+spellname+" has been set to "+ cooldown+"."
    return out_msg
def set_spell_effect(message, spellname, target_dict):
    msg = message.content
    effect = msg.split("set spell effect ", 1)[1]
    target_dict[spellname].effect = effect
    out_msg = "The effect of "+spellname+" has been set to "+ effect+"."
    return out_msg
def set_spell_targets(message, spellname, target_dict):
    msg = message.content
    targets = msg.split("set spell targets ", 1)[1]
    target_dict[spellname].targets = int(targets)
    out_msg = "The targets of "+spellname+" has been set to "+targets +"."
    return out_msg
def set_spell_description(message, spellname, target_dict):
    msg = message.content
    description = msg.split("set spell description ", 1)[1]
    target_dict[spellname].description = description
    out_msg = "The description of "+spellname+" has been set to "+description +"."
    return out_msg
def set_spell_picture(message, spellname, target_dict):
    msg = message.content
    picture_url = msg.split("set spell picture ", 1)[1]
    target_dict[spellname].picture_url = picture_url
    out_msg = "The picture url of "+spellname+" has been set to < "+ picture_url +" >."
    return out_msg
def set_spell_crit_effect(message, spellname, target_dict):
    msg = message.content
    crit_effect = msg.split("set spell crit_effect ", 1)[1]
    target_dict[spellname].crit_effect = crit_effect
    out_msg = "The crit_effect of "+spellname+" has been set to "+crit_effect +"."
    return out_msg
def set_spell_crit_effect_duration(message, spellname, target_dict):
    msg = message.content
    crit_effect_duration = msg.split("set spell crit_effect_duration ", 1)[1]
    target_dict[spellname].crit_effect_duration = int(crit_effect_duration)
    out_msg = "The crit_effect_duration of "+spellname+" has been set to "+ crit_effect_duration+"."
    return out_msg
def set_spell_crit_damage(message, spellname, target_dict):
    msg = message.content
    crit_damage = msg.split("set spell crit_damage ", 1)[1]
    target_dict[spellname].crit_damage = int(crit_damage)
    out_msg = "The crit_damage of "+spellname+" has been set to "+crit_damage +"."
    return out_msg
def set_spell_crit_heal(message, spellname, target_dict):
    msg = message.content
    crit_heal = msg.split("set spell crit_heal ", 1)[1]
    target_dict[spellname].crit_heal = int(crit_heal)
    out_msg = "The crit_heal of "+spellname+" has been set to "+ crit_heal+"."
    return out_msg
def set_spell_effect_duration(message, spellname, target_dict):
    msg = message.content
    effect_duration = msg.split("set spell effect_duration ", 1)[1]
    print(effect_duration)
    target_dict[spellname].effect_duration = int(effect_duration)
    out_msg = "The effect_duration of "+spellname+" has been set to "+ effect_duration+"."
    return out_msg
def set_spell_modifier(message, spellname, target_dict):
    msg = message.content
    modifier = msg.split("set spell modifier ", 1)[1]
    target_dict[spellname].add_modifier = int(modifier)
    out_msg = "The modifier of "+spellname+" has been set to "+ modifier+"."
    return out_msg
def remove_spell(message, target_dict):
    content = message.content.split("remove spell ", 1)[1]
    content = content.split(" ")
    spellname = content[0]
    target_dict.pop(spellname)
    out_msg = spellname+" has been removed from spells."
    return out_msg