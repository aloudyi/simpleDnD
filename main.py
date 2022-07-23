import discord
from os import getenv
from classes.Environment import Environment
from utils.round_utils import play_round

# Initialize the discord client
client = discord.Client()
# Initialize the environment
env = Environment()

out_channel_id = getenv("CHANNEL_ID")

# Monster Management
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    # Reload previous environment
    env.reload_env()

@client.event
async def on_message(message):
    out_channel = client.get_channel(id=out_channel_id)
    play_round(message, env, out_channel)
    
client.run(getenv("TOKEN"))
