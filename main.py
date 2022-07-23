import discord
from os import getenv
from classes.environment import Environment
from round_utils import play_round
from visuals.embed_visuals import get_monster_profile_embed, get_spell_embed
from classes.monster import Monster
from classes.character import Character
from classes.spell import Spell

# Initialize the discord client
client = discord.Client()
# Initialize the environment
env = Environment()

out_channel_id = getenv("CHANNEL_ID")
path_to_save = getenv("PATH_SAVE")
# Monster Management
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    # Reload previous environment
    env.reload_env(path_to_save)

@client.event
async def on_message(message):
    msg = False
    embed = False
    out_channel = client.get_channel(id=out_channel_id)
    msg, embed = play_round(message, env, out_channel)
     
    if (message.content.startswith("!monsters")):
        monsters = env.dict_monsters
        for monster_name in monsters.keys():
            print(monster_name)
            await message.channel.send(embed=get_monster_profile_embed(monster_name, env))
    if (message.content.startswith("!spells")):
        spells = env.dict_spells
        for spell_name in spells.keys():
            print(spell_name)
            await message.channel.send(embed=get_spell_embed(spell_name, env))
    if(msg!=False):
        await message.channel.send(msg)
    if(embed!=False):
        await message.channel.send(embed=embed)
client.run(getenv("TOKEN"))