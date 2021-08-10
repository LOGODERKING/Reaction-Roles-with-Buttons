import discord, os, json
from discord.ext import commands
from discord.ext.commands import CommandNotFound, CommandInvokeError
import datetime as datetime
from discord_components import (DiscordComponents, Button, ButtonStyle, Select, SelectOption)


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='=', intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    DiscordComponents(client)
    print(f'Launched: {client.user.name} // {client.user.id}')

@client.command(description="Loads an extention")
@commands.has_permissions(administrator=True)
async def load(ctx, extention):
    client.load_extension(f'cogs.{extention}')
    await ctx.send(f"**Loaded {extention}**", delete_after=2)

@client.command(description="Unloads an extention")
@commands.has_permissions(administrator=True)
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')
    await ctx.send(f"**Unloaded {extention}**", delete_after=2)

@client.command(description="Reloads an extention")
@commands.has_permissions(administrator=True)
async def reload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')
    client.load_extension(f'cogs.{extention}')
    await ctx.send(f"**Reloaded {extention}**", delete_after=2)

for filename in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cogs')):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded: cog.{filename[:-3]}')




client.run('YOUR BOT TOKEN')
