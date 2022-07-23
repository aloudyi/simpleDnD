import discord
from os import getenv
from utils.entity_utils import *
from utils.spell_utils import *
from utils.environment_utils import monster_join_battle
from utils.character_utils import create_character
from utils.monster_utils import create_monster
from visuals.embed_visuals import battle_summary, get_profile_embed, get_profile_embed, get_monster_profile_embed, get_monster_perception_profile_embed
from classes.spell import Spell
from classes.monster import Monster
from classes.character import Character


brahim_id = getenv("BRAHIM_ID")
path_to_save = getenv("PATH_SAVE")
def character_commands(message, env):
    # Create a character
    # create character race name
    out_message = "Char Command"
    if (message.content.startswith("!create character ")):
        content = message.content.split("!create character ", 1)[1]
        content = content.split(" ")
        race = content[0]
        name = content[1] 
        new_character = Character(name=name,race=race,user_id=user_id)
        out_msg = create_character(new_character, message.author.id, env)
    elif (message.content.startswith("!set name ")):
        name = message.content.split("!set name ", 1)[1]
        out_message = set_entity_name(name, env.dict_characters[message.author.id])
    elif (message.content.startswith("!set race ")):
        race = message.content.split("!set race ", 1)[1]
        out_message = set_entity_race(race, env.dict_characters[message.author.id])
    elif (message.content.startswith("!set current_hp ")):
        current_hp = message.content.split("!set current_hp ", 1)[1]
        out_message = set_entity_current_hp(current_hp,env.dict_characters[message.author.id])
    elif (message.content.startswith("!set max_hp ")):
        max_hp = message.content.split("!set max_hp ", 1)[1]
        out_message = set_entity_max_hp(max_hp, env.dict_characters[message.author.id])
    elif (message.content.startswith("!set state ")):
        state = message.content.split("!set state ", 1)[1]
        out_message = set_entity_state(state, env.dict_characters[message.author.id])
    elif (message.content.startswith("!set modifier ")):
        modifier = message.content.split("!set modifier ", 1)[1]
        out_message = set_entity_modifier(modifier, env.dict_characters[message.author.id])
    elif (message.content.startswith("!set description ")):
        description = message.content.split("!set description ", 1)[1]
        out_message = set_entity_description(description,env.dict_characters[message.author.id])
    elif (message.content.startswith("!set picture ")):
        picture_url = message.content.split("!set picture ", 1)[1]
        out_message = set_entity_picture(picture_url, env.dict_characters[message.author.id])
    elif (message.content.startswith("!set level ")):
        level = message.content.split("!set level ", 1)[1]
        out_message = set_entity_level(level, env.dict_characters[message.author.id])
    elif (message.content.startswith("!set current_xp ")):
        current_xp = message.content.split("!set current_xp ", 1)[1]
        out_message = set_entity_current_xp(current_xp,env.dict_characters[message.author.id])
    elif (message.content.startswith("!set xp_to_next_level ")):
        xp_to_next_level = message.content.split("!set xp_to_next_level ", 1)[1]
        out_message = set_entity_xp_to_next_level(xp_to_next_level,env.dict_characters[message.author.id])
    elif (message.content.startswith("!set state_duration ")):
        state_duration = message.content.split("!set state_duration ", 1)[1]
        out_message = set_entity_state_duration(state_duration,env.dict_characters[message.author.id])
    elif (message.content.startswith("!set user_id ")):
        user_id = message.content.split("!user_id xp_to_next_level ", 1)[1]
        out_message = set_entity_user_id(user_id, env.dict_characters[message.author.id])  
    return out_message

def monster_commands(message, env):
    out_msg = "Monster Command Failed !"
    if (message.content.startswith("!create monster ")):
        content = message.content.split("!create monster ", 1)[1]
        content = content.split(" ")
        race = content[0]
        name = content[1]
        new_monster = Monster(name,race)
        out_msg = create_monster(new_monster, env)
    # Set monster parameters
    elif (message.content.startswith("!monster ")):
        content = message.content.split("!monster ", 1)[1]
        content = content.split(" ")
        monster_name = content[0]
        message.content = " ".join(content[1:])
        if (message.content.startswith("set race ")):
            race = message.content.split("set race ", 1)[1]
            out_msg = set_entity_race(race, env.dict_monsters[monster_name])
        elif (message.content.startswith("set class ")):
            monster_class = message.content.split("set class ", 1)[1]
            out_msg = set_entity_class(monster_class, env.dict_monsters[monster_name])        
        elif (message.content.startswith("set rename ")):
            custom_name = message.content.split("set rename ", 1)[1]
            out_msg = set_entity_name(custom_name,env.dict_monsters[monster_name])
        elif (message.content.startswith("set current_hp ")):
            current_hp = message.content.split("set current_hp ", 1)[1]
            out_msg = set_entity_current_hp(current_hp, env.dict_monsters[monster_name])
        elif (message.content.startswith("set max_hp ")):
            max_hp = message.content.split("set max_hp ", 1)[1]
            out_msg = set_entity_max_hp(max_hp, env.dict_monsters[monster_name])
        elif (message.content.startswith("set state ")):
            state = message.content.split("set state ", 1)[1]
            out_msg = set_entity_state(state, env.dict_monsters[monster_name])
        elif (message.content.startswith("set modifier ")):
            modifier = message.content.split("set modifier ", 1)[1]
            out_msg = set_entity_modifier(modifier, env.dict_monsters[monster_name])
        elif (message.content.startswith("set description ")):
            description = message.content.split("set description ", 1)[1]
            out_msg = set_entity_description(description, env.dict_monsters[monster_name])
        elif (message.content.startswith("set picture ")):
            picture_url = message.content.split("set picture ", 1)[1]
            out_msg = set_entity_picture(picture_url, env.dict_monsters[monster_name])
        elif (message.content.startswith("join battle ")):
            custom_name = message.content.split("join battle ")[1]
            monster_join_battle(custom_name, monster_name, env)
            out_msg = "A monster just joined the battle !"
        return out_msg        

def player_attack_monster_command(message, env):
    if (message.content.startswith("*")):
        content = message.content.split("*", 1)[1]
        content = content.split(" ")
        spellname = content[0]
        target = content[1]
        caster = env.dict_characters[message.author.id]
        target = env.dict_battle[target]
        embed_out = battle_summary(caster, spellname, target, env)
        return embed_out

def monster_attack_player_command(message, env):
    if (message.content.startswith("&")):
        content = message.content.split("&", 1)[1]
        content = content.split(" ")
        caster = content[0]
        spellname = content[1]
        target = content[2]
        caster = env.dict_battle[caster]
        if (target in env.dict_battle.keys()):
            target = env.dict_battle[target]
        else:
            for key in env.dict_characters:
                char = env.dict_characters[key]
                if (char.name == target):
                    target = char
        embed_out = battle_summary(caster, spellname, target, env)
        return embed_out

def player_attack_player_command(message, env):
    if (message.content.startswith("pvp")):
        content = message.content.split("pvp ", 1)[1]
        content = content.split(" ")
        spellname = content[0]
        target_name = content[1]
        caster = env.dict_characters[message.author.id]
        for key in env.dict_characters.keys():
            if (env.dict_characters[key].name == target_name):
                target = env.dict_characters[key]
        embed_out = battle_summary(caster, spellname, target, env)
        return embed_out

def spell_commands(message, env):
    out_msg = "Spell Command Failed !"
    if (message.content.startswith("!create spell ")):
        content = message.content.split("!create spell ", 1)[1]
        spellname = content.split(" ")[0]
        new_spell = Spell(new_spell)
        out_msg = create_spell(new_spell, env)
    elif (message.content.startswith("!linkspell ")):
        content = message.content.split("!linkspell ", 1)[1]
        if (content.startswith("monster")):
            content = content.split("monster ", 1)[1]
            content = content.split(" ")
            name = content[0]
            spellname = content[1]
            entity = env.dict_monsters[name]
            out_msg = link_spell(entity, spellname, env.dict_spells)
            out_msg = out_msg +"the monster class "+name+" !"
        elif (content.startswith("character")):
            content = content.split("character ", 1)[1]
            content = content.split(" ")
            name = content[0]
            spellname = content[1]
            for key in env.dict_characters.keys():
                if (env.dict_characters[key].name == name):
                    entity = env.dict_characters[key]
                    out_msg = link_spell(entity, spellname, env.dict_spells)
                    out_msg = out_msg +"the character "+name+" !"
    elif (message.content.startswith("!edit spell ")):
        content = message.content.split("!edit spell ", 1)[1]
        content = content.split(" ")
        spellname = content[0]
        message.content = " ".join(content[1:])
        if (message.content.startswith("set spell success ")):
            out_msg = set_spell_success(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell type ")):
            out_msg = set_spell_type(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell crit ")):
            out_msg = set_spell_crit(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell damage ")):
            out_msg = set_spell_damage(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell current_cooldown ")):
            out_msg = set_spell_current_cooldown(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell cooldown ")):
            out_msg = set_spell_cooldown(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell effect ")):
            out_msg = set_spell_effect(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell targets ")):
            out_msg = set_spell_targets(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell description ")):
            out_msg = set_spell_description(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell modifier ")):
            out_msg = set_spell_modifier(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell crit_damage ")):
            out_msg = set_spell_crit_damage(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell picture ")):
            out_msg = set_spell_picture(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell heal ")):
            out_msg = set_spell_heal(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell crit_effect ")):
            out_msg = set_spell_crit_effect(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell crit_effect_duration ")):
            out_msg = set_spell_crit_effect_duration(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell crit_heal ")):
            out_msg = set_spell_crit_heal(message, spellname, env.dict_spells)
        elif (message.content.startswith("set spell effect_duration ")):
            out_msg = set_spell_effect_duration(message, spellname, env.dict_spells)
    elif (message.content.startswith("!remove spell ")):
        out_msg = remove_spell(message, env.dict_characters[message.author.id].spells)
    return out_msg

def battle_commands(message, env):
    embed = False
    if (message.content.startswith("!battle state")):
        battle = env.dict_battle
        embed = discord.Embed()
        embed.set_author(name="BattleState")
        for mobkey in battle.keys():
            mob_name = mobkey
            mob_hp = str(battle[mobkey].current_hp)
            mob_max_hp = str(battle[mobkey].max_hp)
            value = "HitPoints : " + mob_hp + "/" + mob_max_hp
            embed.add_field(name=mob_name, value=value)
    elif (message.content.startswith("!battle clear")):
        env.dict_battle = {}
        embed.add_field(name = "Battle Cleared", value = f"Requested by <@{message.author.id}>")
    elif (message.content.startswith("!battle perception ")):
        battle_monster_name = message.content.split("!battle perception ", 1)[1]
        embed = get_monster_perception_profile_embed(battle_monster_name, message.author.id, env)
    return embed

def debug_command():
    return f"mamak zwina <@{brahim_id}>"

def play_round(message, env, out_channel):
    
    msg = False
    embed = False
    
    if(message.content.startswith("!set") or message.content.startswith("!create character ")):
        msg = character_commands(message, env)

    if(message.content.startswith("!monster" )):
        msg = monster_commands(message, env)
 
    if(message.content.startswith("*")):
        embed = player_attack_monster_command(message, env)
    
    if(message.content.startswith("&")):
        embed = monster_attack_player_command(message, env)

    if(message.content.startswith("pvp ")):
        embed = player_attack_player_command(message, env)

    if(message.content.startswith("!edit spell ") or message.content.startswith("!create spell ") or message.content.startswith("!linkspell ")):
        msg = spell_commands(message, env)

    if(message.content.startswith("!battle ")): 
        embed = battle_commands(message, env)

    if (message.content.startswith("debug")):
        msg = debug_command()
    
    ### Information commands
    if (message.content.startswith("!profile")):
        embed = get_profile_embed(message.author.id, env)
    elif (message.content.startswith("!bestiary ")):
        monster_name = message.content.split("!bestiary ", 1)[1]
        embed = get_monster_profile_embed(monster_name, env)
    elif (message.content.startswith("!save")):
        env.save_env(path_to_save)
        embed.add_field(name="Save", value="Saved the advancement successfully !")

    # Save environment at each command
    env.save_env(path_to_save)

    return msg, embed
