import discord
from os import getenv
from utils.entity_utils import *
from utils.spell_utils import *
from utils.environment_utils import monster_join_battle
from utils.character_utils import create_character
from utils.monster_utils import create_monster
from visuals.embed_visuals import battle_summary, get_profile_embed, get_profile_embed, get_monster_profile_embed, get_monster_perception_profile_embed, get_spell_embed
from classes.spell import Spell
from classes.monster import Monster
from classes.character import Character
from classes.dungeon import Dungeon
from classes.room import Room
from pathlib import Path

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
        new_character = Character(name=name,race=race,user_id=message.author.id)
        out_message = create_character(new_character, message.author.id, env)
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
        print(out_msg)
    # Set monster parameters
    elif (message.content.startswith("!monster remove ")):
        monster_name = message.content.split("!monster remove ")[1]
        env.dict_monsters.pop(monster_name)
        out_msg = monster_name+" has been removed from monsters."
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
        new_spell = Spell(spellname)
        out_msg = create_spell(new_spell, env)
    elif(message.content.startswith("!linkspell ")):
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
        embed.set_author(name="BattleState : "+env.current_room_name)
        value = "No ennemies :c"
        field_name = "There are no ennemies on the field currently."
        for mobkey in battle.keys():
            value = value+" -> "+mobkey+"\n"
            field_name = "Ennemies are on the field !"
        embed.add_field(name=field_name, value=value,inline=False)
    elif (message.content.startswith("!battle clear")):
        env.dict_battle = {}
        embed = discord.Embed()
        embed.add_field(name = "Battle Cleared", value = f"Requested by <@{message.author.id}>")
    elif (message.content.startswith("!battle perception ")):
        battle_monster_name = message.content.split("!battle perception ", 1)[1]
        embed = get_monster_perception_profile_embed(battle_monster_name, message.author.id, env)
    return embed

def debug_command(env):
    return f"mamak zwina <@{brahim_id}>"

def dungeon_commands(message, env):
    out_msg = "Dungeon Command Failed !"
    if(message.content.startswith("!create dungeon")):
        dungeon_name = message.content.split("!create dungeon ", 1)[1]
        dungeon = Dungeon(dungeon_name)
        env.add_dungeon(dungeon)
        out_msg = "The dungeon "+dungeon_name+" has been added to the environment."
    elif(message.content.startswith("!dungeon ")):
        content = message.content.split("!dungeon ", 1)[1]
        content = content.split(" ")
        dungeon_name = content[0]
        dungeon = env.dict_dungeons[dungeon_name]
        message.content = " ".join(content[1:])
        if(message.content.startswith("set room ")):
            content = message.content.split("set room ",1)[1]
            if(content.startswith("name")):
                room_name = content.split("name ",1)[1]
                room = Room(room_name)
                dungeon.add_room(room)
                out_msg = "The room "+room_name+" has been added to the dungeon "+ dungeon_name
            elif(content.startswith("monsters ")):
                content = content.split("monsters ",1)[1]
                if(content.startswith("add ")):
                    content = content.split("add ",1)[1]
                    content = content.split(" ")
                    room_name = content[0]
                    monster_name = content[1]
                    custom_name = content[2]
                    monster = env.get_monster(monster_name)
                    monster.name = custom_name
                    dungeon.dict_rooms[room_name].add_monster(monster)
                    out_msg = monster.name +" has been added to the dungeon "+dungeon.name+" at room "+room_name
                elif(content.startswith("remove ")):
                    content = content.split("remove ",1)[1]
                    content = content.split(" ")
                    room_name = content[0]
                    monster_name = content[1]
                    dungeon.dict_rooms[room_name].remove_monster(monster_name)
                    out_msg = monster_name +" has been removed from the dungeon "+dungeon.name+" at room "+room_name
    elif(message.content.startswith("!load dungeon ")):
        dungeon_name = message.content.split("!load dungeon ",1)[1]
        env.load_dungeon(dungeon_name)
        out_msg = dungeon_name+" has been loaded as the current dungeon."
    elif(message.content.startswith("!load room")):
        room_name = message.content.split("!load room ",1)[1]
        env.load_room(room_name)
        out_msg = room_name+" has been loaded as the current room."

    
    return out_msg
                
def play_round(message, env, out_channel):
    
    msg = False
    embed = False
    
    if(message.content.startswith("!set") or message.content.startswith("!create character ")):
        msg = character_commands(message, env)

    if(message.content.startswith("!monster " ) or message.content.startswith("!create monster " )):
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
        msg = debug_command(env)
    
    if(message.content.startswith("!create dungeon") or message.content.startswith("!dungeon") or message.content.startswith("!load dungeon ") or message.content.startswith("!load room")):
        msg = dungeon_commands(message, env)

    ### Information commands
    if (message.content.startswith("!profile")):
        embed = get_profile_embed(message.author.id, env)
    elif(message.content.startswith("!spellbook ")):
        spellname = message.content.split("!spellbook ", 1)[1]
        embed = get_spell_embed(spellname,env)
    elif (message.content.startswith("!bestiary ")):
        monster_name = message.content.split("!bestiary ", 1)[1]
        embed = get_monster_profile_embed(monster_name, env)
    elif (message.content.startswith("!save")):
        env.save_env(path_to_save)
        embed = discord.Embed()
        embed.add_field(name="Save", value="Saved the advancement successfully !")
    elif(message.content.startswith("!help ")):
        content = message.content.split("!help ",1)[1]
        msg = Path("help_"+content+".md").read_text()
    elif(message.content.startswith("!help")):
        msg = "You can use !help followed with monster, spell, character, dungeon or misc to see extra informations."

    env.save_env(path_to_save)

    return msg, embed
