import discord
import asyncio
import random
import time

client = discord.Client()

@client.event
async def on_message(message):
    AUTHOR_ID = 410561838791786507
    emojis_m = ["🇱", "🇮", "🇳", "🇩", "🇴"]
    if(message.author.id == AUTHOR_ID):
        for emoji in emojis_m:
            await message.add_reaction(emoji)
    

token = "Njc0MDQ2MDM4NzU1MTE1MDM4.Xji42g.JTHury5_1OWqonROdjx70Ur6rlY"
client.run(token)