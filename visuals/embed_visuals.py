import discord
from numpy.random import randint
from os import getenv

question_mark_pic = getenv("QUESTION_MARK")

def battle_summary(caster, spellname, target, env):
    target_old_hp = target.current_hp
    #Use spell
    embed = discord.Embed(color=0xFF5733)
    # Author name & Author Icon
    embed.set_author(name=caster.name, icon_url=caster.picture_url)
    if (caster.state == "stunned"):
        if (caster.state_duration == 0):
            caster.state = "normal"
        else:
            caster.state_duration -= 1
            embed.add_field(
                name="BattleRecap",value="You are **STUNNED**, you can't play this turn.")
            return embed
    if(caster.spells[spellname]!=0):
        embed.add_field(name="BattleRecap",value="You can't use this spell now, it's on **COOLDOWN ("+str(caster.spells[spellname])+")** !!")
        return embed
    else:
        battle_recap, dice_roll, modifier, message = env.use_spell(caster, spellname, target,env)
        # Battle recap
        if (modifier != 0):
            modifier_txt = "+ " + str(modifier)
        else:
            modifier_txt = ""
        embed.set_thumbnail(url=target.picture_url)
        roll = "You rolled " + str(dice_roll) + modifier_txt + " (**" + str(
            dice_roll + modifier) + "**)."
        msg = battle_recap + "\n" + roll
        embed.add_field(name="BattleRecap :", value=msg, inline=False)
        if (caster.state == "stunned"):
            duration = "(" + str(caster.state_duration) + ")"
        else:
            duration = ""
        caster_msg = "**HitPoints** : " + str(caster.current_hp) + "/*" + str(
            caster.max_hp) + "*\n **State** : *" + caster.state + duration + "*."

        if (target.state == "stunned"):
            duration = "(" + str(target.state_duration) + ")"
        else:
            duration = ""
        target_msg = "**HitPoints** : " + str(
            target.current_hp
        ) + "(" + str(-target_old_hp + target.current_hp) + ")/*" + str(
            target.max_hp) + "*\n **State** : *" + target.state + duration + "*."
        embed.add_field(name=caster.name, value=caster_msg, inline=True)
        embed.add_field(name=target.name, value=target_msg, inline=True)
        if(message!="blank"):
            embed = discord.Embed(color=0xFF5733)
            embed.add_field(name="ALaAaAARM",value=message)
    return embed

# Returs a spell summary embed
def get_spell_embed(spellname, env):
    spell = env.dict_spells[spellname]

    embed = discord.Embed(color=0x5733FF)
    # Spell Picture
    if (spell.picture_url != ""):
        embed.set_thumbnail(url=spell.picture_url)

    # Spell Summary
    name = spellname
    targets = str(spell.targets)
    effect = spell.effect
    cooldown = str(spell.cooldown)
    add_modifier = str(spell.add_modifier)
    type = spell.type
    embed.set_author(name="Spell Summary")
    value = "Type : " + type + "\nTargets : " + targets + "\nCooldown : " + cooldown + "\nModifier: " + add_modifier
    embed.add_field(name=name, value=value, inline=False)

    # Normal
    title = "Normal Effects"
    success = str(spell.success_condition)
    damage = str(spell.damage)
    heal = str(spell.heal)

    effect_duration = str(spell.effect_duration)
    value = "Effect : " + effect + "\nSuccess Roll >= " + success + "\nEffect Duration :" + effect_duration + "\nDamage : " + damage + "\nHeal : " + heal
    embed.add_field(name=title, value=value)

    if (spell.type == "normal"):
        # Crit
        title = "Critical Effects"
        success = str(spell.crit_condition)
        effect = spell.crit_effect

        damage = str(spell.crit_damage + spell.damage)
        heal = str(spell.heal + spell.crit_heal)
        effect_duration = str(spell.crit_effect_duration +
                              spell.effect_duration)

        value = "Critical Effect : " + effect + "\nCritical Success Roll >= " + success + "\nCritical Effect Duration :" + effect_duration + "\nCritical Damage : " + damage + "\nCritical Heal : " + heal
    elif (spell.type == "double-edge"):
        title = "Negative Effects"
        success = str(spell.success_condition)
        effect = spell.crit_effect

        damage = str(spell.crit_damage)
        heal = str(spell.crit_heal)
        effect_duration = str(spell.effect_duration)
        value = "Negative Effect : "+effect+"\nSuccess Roll < " + success + "\nEffect Duration :" + effect_duration + "\nDamage : " + damage + "\nHeal : " + heal
    embed.add_field(name=title, value=value)
    return embed

# Returns the character profile
def get_profile_embed(user_id, env):
        char = env.dict_characters[user_id]
        name = char.name
        level = str(char.level)
        race = char.race
        xp = str(char.current_xp)
        next_level = str(char.xp_to_next_level)
        spellnames = [spell for spell in char.spells.keys()]
        profile_pic = char.picture_url
        hp = str(char.current_hp)
        max_hp = str(char.max_hp)

        embed = discord.Embed(color=0xFF5733)
        embed.set_author(name=name)
        if (profile_pic != ""):
            embed.set_thumbnail(url=profile_pic)
        field_value = "Name : " + name + "\nRace: " + race + "\nLevel : " + level + "\nHitPoints : " + hp + "/" + max_hp + "\nXP : " + xp + "/" + next_level + "\nSpells : "
        for spellname in spellnames:
            field_value = field_value + "\n* " + spellname + "."
        embed.add_field(name="Profile", value=field_value)
        embed.add_field(name="Description", value=char.description, inline=False)
        return embed

# Returns a monster's embed
def get_monster_profile_embed(name, env):
    char = env.dict_monsters[name]
    name = char.name
    race = char.race
    spellnames = [spell for spell in char.spells.keys()]
    profile_pic = char.picture_url
    hp = str(char.current_hp)
    max_hp = str(char.max_hp)
    embed = discord.Embed(color=0xFF5733)
    embed.set_author(name=name)
    if (profile_pic != ""):
        embed.set_thumbnail(url=profile_pic)
    field_value = "Name : " + name + "\nRace: " + race + "\nHitPoints : " + hp + "/" + max_hp + "\nSpells : "
    for spellname in spellnames:
        field_value = field_value + "\n* " + spellname + "."
    print(9)
    print(char)
    print(char.description)
    embed.add_field(name="Profile", value=field_value)
    print(char.description)
    embed.add_field(name="Description", value=char.description, inline=False)
    return embed

# Returns a preception roll on a monster
def get_monster_perception_profile_embed(name, user_id, env):
    perception_roll = randint(1, 21)
    char = env.dict_battle[name]

    name = char.name
    if (perception_roll >= 10):
        race = char.race
        monster_class = char.monster_class
    else:
        race = "????"
        monster_class = "????"
    if (perception_roll > 10):
        description = char.description
    else:
        description = "?????"
    if (perception_roll >= 12):
        profile_pic = char.picture_url
    else:
        profile_pic = question_mark_pic
    if (perception_roll >= 14):
        spellnames = [spell for spell in char.spells.keys()]
    else:
        spellnames = []
    if (perception_roll >= 15):
        hp = str(char.current_hp)
        max_hp = str(char.max_hp)
    else:
        hp = "??"
        max_hp = "??"
    embed = discord.Embed(color=0xFF5733)
    embed.set_author(name=name)
    if (profile_pic != ""):
        embed.set_thumbnail(url=profile_pic)
    field_value = "Name : " + name + "\nClass: " + monster_class + "\nRace: " + race + "\nHitPoints : " + hp + "/" + max_hp + "\nSpells : "
    for spellname in spellnames:
        field_value = field_value + "\n* " + spellname + "."
    embed.add_field(name="Profile", value=field_value)
    embed.add_field(name="Description", value=description, inline=False)
    text = env.dict_characters[user_id].name + " rolled **" + str(
        perception_roll) + "** on his perception roll."
    embed.description = text
    return embed