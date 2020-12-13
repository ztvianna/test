
# Import Discord Package
import discord

from discord.ext import commands
import random

# Import our configuration
import config
from cards import *

# Initialize our Discord client, channel configuration, and game state
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix='!')
gameRunning = False


def hand():
    hand_cards = dict()
    hand_cards['white'] = random.sample(white_cards, k=4)
    hand_cards['red'] = random.sample(red_cards, k=3)
    return hand_cards

# the first client event was just a test. the second one is for the DM
@client.event
async def on_message(message):
    game_channel = client.get_channel(config.game_channel_id)
    if message.content == 'play':
        await game_channel.send('hello')

    if message.content == "hello?":
        await message.author.send('hi?')

    if message.content == "hand":
        await game_channel.send('Sending Hands')
        for member in game_channel.members:
            player = await client.fetch_user(member.id)
            player_hand = hand()

            ## Some users don't accept messages from strangers. We need to handle that case. 
            try: 
                await player.send('Here\'s your hand!')
                await player.send('**White:** ')
                await player.send("\n".join(player_hand['white']))
                await player.send('**Red:** ')
                await player.send("\n".join(player_hand['red']))

            except: 
                pass        

print("Running Red Flags Game Server")

#Run the client on the server
client.run(config.bot_token)


