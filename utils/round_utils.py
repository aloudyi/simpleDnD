import discord
from os import getenv
from classes.Environment import Environment
from classes.Character import Character
from classes.Monster import Monster
from utils.entity_utils import *
from utils.spell_utils import *
from utils.environment_utils import monster_join_battle
from utils.character_utils import create_character
from utils.monster_utils import create_monster
from visuals.embed_visuals import battle_summary, get_profile_embed, get_profile_embed, get_monster_profile_embed, get_monster_perception_profile_embed

brahim_id = getenv("BRAHIM_ID")

async def character_commands(message, env):
    # Create a character
    # create character race name
    if (message.content.startswith("!create character ")):
        content = message.content.split("!create character ", 1)[1]
        create_character(content, message.author.id, env)
    elif (message.content.startswith("!set name ")):
        name = message.content.split("!set name ", 1)[1]
        set_entity_name(name, env.dict_characters[message.author.id])
    elif (message.content.startswith("!set race ")):
        race = message.content.split("!set race ", 1)[1]
        set_entity_race(race, env.dict_characters[message.author.id])
    elif (message.content.startswith("!set current_hp ")):
        current_hp = message.content.split("!set current_hp ", 1)[1]
        set_entity_current_hp(current_hp,env.dict_characters[message.author.id])
    elif (message.content.startswith("!set max_hp ")):
        max_hp = message.content.split("!set max_hp ", 1)[1]
        set_entity_max_hp(max_hp, env.dict_characters[message.author.id])
    elif (message.content.startswith("!set state ")):
        state = message.content.split("!set state ", 1)[1]
        set_entity_state(state, env.dict_characters[message.author.id])
    elif (message.content.startswith("!set modifier ")):
        modifier = message.content.split("!set modifier ", 1)[1]
        set_entity_modifier(modifier, env.dict_characters[message.author.id])
    elif (message.content.startswith("!set description ")):
        description = message.content.split("!set description ", 1)[1]
        set_entity_description(description,env.dict_characters[message.author.id])
    elif (message.content.startswith("!set picture ")):
        picture_url = message.content.split("!set picture ", 1)[1]
        set_entity_picture(picture_url, env.dict_characters[message.author.id])
    elif (message.content.startswith("!set level ")):
        level = message.content.split("!set level ", 1)[1]
        set_entity_level(level, env.dict_characters[message.author.id])
    elif (message.content.startswith("!set current_xp ")):
        current_xp = message.content.split("!set current_xp ", 1)[1]
        set_entity_current_xp(current_xp,env.dict_characters[message.author.id])
    elif (message.content.startswith("!set xp_to_next_level ")):
        xp_to_next_level = message.content.split("!set xp_to_next_level ", 1)[1]
        set_entity_xp_to_next_level(xp_to_next_level,env.dict_characters[message.author.id])
    elif (message.content.startswith("!set state_duration ")):
        state_duration = message.content.split("!set state_duration ", 1)[1]
        set_entity_state_duration(state_duration,env.dict_characters[message.author.id])
    elif (message.content.startswith("!set user_id ")):
        user_id = message.content.split("!user_id xp_to_next_level ", 1)[1]
        set_entity_user_id(user_id, env.dict_characters[message.author.id])  

async def monster_commands(message, env, out_channel):
    if (message.content.startswith("!create monster ")):
        content = message.content.split("!create monster ", 1)[1]
        create_monster(content, env)
    # Set monster parameters
    elif (message.content.startswith("!monster ")):
        content = message.content.split("!monster ", 1)[1]
        content = content.split(" ")
        monster_name = content[0]
        message.content = " ".join(content[1:])
        if (message.content.startswith("set race ")):
            race = message.content.split("set race ", 1)[1]
            set_entity_race(race, env.dict_monsters[monster_name])
        elif (message.content.startswith("set class ")):
            monster_class = message.content.split("set class ", 1)[1]
            env.dict_monsters[monster_name].monster_class = monster_class
        elif (message.content.startswith("set name ")):
            custom_name = message.content.split("set name ", 1)[1]
            monster = env.dict_monsters[monster_name]
            env.dict_monsters.pop(monster_name)
            monster.name = custom_name
            env.dict_monsters[custom_name] = monster
        elif (message.content.startswith("set current_hp ")):
            current_hp = message.content.split("set current_hp ", 1)[1]
            set_entity_current_hp(current_hp, env.dict_monsters[monster_name])
        elif (message.content.startswith("set max_hp ")):
            max_hp = message.content.split("set max_hp ", 1)[1]
            set_entity_max_hp(max_hp, env.dict_monsters[monster_name])
        elif (message.content.startswith("set state ")):
            state = message.content.split("set state ", 1)[1]
            set_entity_state(state, env.dict_monsters[monster_name])
        elif (message.content.startswith("set modifier ")):
            modifier = message.content.split("set modifier ", 1)[1]
            set_entity_modifier(modifier, env.dict_monsters[monster_name])
        elif (message.content.startswith("set description ")):
            description = message.content.split("set description ", 1)[1]
            set_entity_description(description, env.dict_monsters[monster_name])
        elif (message.content.startswith("set picture ")):
            picture_url = message.content.split("set picture ", 1)[1]
            set_entity_picture(picture_url, env.dict_monsters[monster_name])
        elif (message.content.startswith("join battle ")):
            custom_name = message.content.split("join battle ")[1]
            monster_join_battle(custom_name, monster_name, env)
            await out_channel.send("A monster just joined the battle !")

async def player_attack_monster_command(message, env):
    if (message.content.startswith("*")):
        content = message.content.split("*", 1)[1]
        content = content.split(" ")
        spellname = content[0]
        target = content[1]
        caster = env.dict_characters[message.author.id]
        target = env.dict_battle[target]
        embed_out = battle_summary(caster, spellname, target, env)
        await message.channel.send(embed=embed_out)

async def monster_attack_player_command(message, env):
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
        await message.channel.send(embed=embed_out)

async def player_attack_player_command(message, env):
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
        await message.channel.send(embed=embed_out)

async def spell_commands(message, env):
    if (message.content.startswith("!create spell ")):
        content = message.content.split("!create spell ", 1)[1]
        spellname = content.split(" ")[0]
        create_spell(spellname, env)
    elif (message.content.startswith("!linkspell ")):
        content = message.content.split("!linkspell ", 1)[1]
        if (content.startswith("monster")):
            content = content.split("monster ", 1)[1]
            content = content.split(" ")
            name = content[0]
            spellname = content[1]
            entity = env.dict_monsters[name]
            link_spell(entity, spellname, env.dict_spells)
        elif (content.startswith("character")):
            content = content.split("character ", 1)[1]
            content = content.split(" ")
            name = content[0]
            spellname = content[1]
            for key in env.dict_characters.keys():
                if (env.dict_characters[key].name == name):
                    entity = env.dict_characters[key]
                    link_spell(entity, spellname, env.dict_spells)
    elif (message.content.startswith("!edit spell ")):
        content = message.content.split("!edit spell ", 1)[1]
        content = content.split(" ")
        spellname = content[0]
        message.content = " ".join(content[1:])
        if (message.content.startswith("set spell success ")):
            set_spell_success(spellname, env.dict_spells)
        elif (message.content.startswith("set spell type ")):
            set_spell_type(spellname, env.dict_spells)
        elif (message.content.startswith("set spell crit ")):
            set_spell_crit(spellname, env.dict_spells)
        elif (message.content.startswith("set spell damage ")):
            set_spell_damage(spellname, env.dict_spells)
        elif (message.content.startswith("set spell current_cooldown ")):
            set_spell_current_cooldown(spellname, env.dict_spells)
        elif (message.content.startswith("set spell cooldown ")):
            set_spell_cooldown(spellname, env.dict_spells)
        elif (message.content.startswith("set spell effect ")):
            set_spell_effect(spellname, env.dict_spells)
        elif (message.content.startswith("set spell targets ")):
            set_spell_targets(spellname, env.dict_spells)
        elif (message.content.startswith("set spell description ")):
            set_spell_description(spellname, env.dict_spells)
        elif (message.content.startswith("set spell modifier ")):
            set_spell_modifier(spellname, env.dict_spells)
        elif (message.content.startswith("set spell crit_damage ")):
            set_spell_crit_damage(spellname, env.dict_spells)
        elif (message.content.startswith("set spell picture ")):
            set_spell_picture(spellname, env.dict_spells)
        elif (message.content.startswith("set spell heal ")):
            set_spell_heal(spellname, env.dict_spells)
        elif (message.content.startswith("set spell crit_effect ")):
            set_spell_crit_effect(spellname, env.dict_spells)
        elif (message.content.startswith("set spell crit_effect_duration ")):
            set_spell_crit_effect_duration(spellname, env.dict_spells)
        elif (message.content.startswith("set spell crit_heal ")):
            set_spell_crit_heal(spellname, env.dict_spells)
        elif (message.content.startswith("set spell effect_duration ")):
            set_spell_effect_duration(spellname, env.dict_spells)
    elif (message.content.startswith("!remove spell ")):
        remove_spell( env.dict_characters[message.author.id].spells)

async def battle_commands(message, env):
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
        await message.channel.send(embed=embed)
    elif (message.content.startswith("!battle clear")):
        env.dict_battle = {}
        await message.channel.send(f"Battle Cleared ! requested by <@{message.author.id}>")
    elif (message.content.startswith("!battle perception ")):
        battle_monster_name = message.content.split("!battle perception ", 1)[1]
        embed = get_monster_perception_profile_embed(battle_monster_name, message.author.id, env)
        await message.channel.send(embed=embed)

async def debug_command(message):
    if (message.content.startswith("debug")):
        await message.channel.send(f"mamak zwina <@{brahim_id}>")

async def information_commands(message, env):
    if (message.content.startswith("!profile")):
        embed = get_profile_embed(message.author.id, env)
        await message.channel.send(embed=embed)
    elif (message.content.startswith("!bestiary ")):
        monster_name = message.content.split("!bestiary ", 1)[1]
        embed_out = get_monster_profile_embed(monster_name, env)
        await message.channel.send(embed=embed_out)
    elif (message.content.startswith("!save")):
        env.save_env()
        await message.channel.send("Saved the advancement successfully !")

async def play_round(message, env, out_channel):
    character_commands(message, env)
    monster_commands(message, env, out_channel)
    player_attack_monster_command(message, env)
    monster_attack_player_command(message, env)
    player_attack_player_command(message, env)
    spell_commands(message, env)
    battle_commands(message, env)
    debug_command(message, message)
    information_commands(message, env)
    env.save_env()