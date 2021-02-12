# Python 3.8.7
import discord
from discord.ext import commands
import scrython
import asyncio
import readLine 
# asyncio does not allow its event loop to be nested, nest_asyncio fixes that!
import nest_asyncio
nest_asyncio.apply()

token = readLine.read_line("token.txt", 0)

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(f"{message.guild}: {message.channel}: {message.author}: {message.content}")
    # If the bot is the writer, don't do anything
    if message.author == client.user:
        return


    if "[[" and "]]" in message.content.lower():
        m = message.content.lower()

        # Find the card inside the message
        start = m.find('[[') + 2
        end = m.find(']]', start)
        cardName = m[start:end]

        await asyncio.sleep(0.1)
        card = scrython.cards.Named(fuzzy=cardName)
        
        imgLink = card.image_uris(0, 'normal')
        print(imgLink)

        await message.channel.send(imgLink) # Send back the card in chat
    

client.run(token)