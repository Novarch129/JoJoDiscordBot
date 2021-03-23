from keep_alive import keep_alive
from discord.ext import commands
import discord.utils
import discord
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$no'):
        await message.channel.send('OK!')
        role = discord.utils.get(message.guild.roles, id=823837011815301170)
        async for member in message.guild.fetch_members(limit=None):
          if member.id == 458184198994395146:
            continue
          await member.add_roles(role)
          print(member.name)
          #await message.channel.send(member.name)

@client.event
async def on_reaction_add(reaction, user):
    role = discord.utils.get(user.guild.roles, id=823837011815301170)
    #await reaction.message.channel.send("Role = {}".format(role.mention))
    await user.add_roles(role)
    
keep_alive()
client.run(os.getenv("TOKEN"))