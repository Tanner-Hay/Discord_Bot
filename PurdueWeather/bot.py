import discord
import asyncio
import os
from secret import TOKEN as token 
from discord.ext import commands, tasks
from Scrape import Weather


client = discord.Client()
channel = client.get_channel(680972360299577396)
weather = Weather()

@client.event
async def on_ready():
    
    print("Bot is logined")
    print(client.user.name)
    print(client.user.id)
    print("----------")

def doathing():
    return "I DID THE THING"

async def background_loop():
    await client.wait_until_ready()
    counter = 0
    while counter is not 10:
        c = client.get_channel(680972360299577396)
        printWords = weather.createForecast()
        await c.send(printWords)
        print(counter)
        await asyncio.sleep(10)

@client.event
async def on_message(message):
    if message.content == '!do a thing':
        s = str(doathing())
        await message.channel.send(s)

    if client.user in message.mentions:
        await message.channel.send('@{}{}'.format(message.author.mention," whats poppin"))

client.loop.create_task(background_loop())
client.run(token)