import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    Dresden_Files_quotes = [
        'You are a drug dealer. To tiny faeries. Shame.',
        'I am not a pessimist," I said loftily. "Though that can\'t last.',
        'Molly once burned my egg. My boiled egg. I don\'t know how.',
        'He had hard, steady eyes, and all the comforting, reassuring charm of a dental drill.',
    ]
# The Dresden books, not the show. The show is terrible.

    King_Killer_quotes = [
        'The best lies about me are the ones I told.',
        'He taught only one class: Unlikely Maths. But since the times was listed as "now" and the place, "everywhere," this was hardly helpful.',
        'Mooooo.',
        'Upon him I will visit famine and fire, Till all-around him desolation rings and all the demons in the outer dark look on amazed and recognize that vengence is the business of a man.',
    ]

    if message.content == 'Dresden':
        response = random.choice(Dresden_Files_quotes)
        await message.channel.send(response)
    elif message.content == 'Wind':    
        response = random.choice(King_Killer_quotes)
        await message.channel.send(response)

client.run(TOKEN)
