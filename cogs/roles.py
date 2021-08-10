import discord, os, os.path, json, asyncio, random
from discord.ext import commands
from discord.utils import get, find
from discord.ext.commands import has_permissions
import datetime as datetime
from discord_components import *


class Roles(commands.Cog):
    def __init__(self, client):
        self.client = client



    # you can use green, blue, grey for the button colors
    # in the label='name' you can change the button name
    # put an emoji within the label='name' to use an emoji
    # WARNING: You can only have 5 emojis per array
    # If you get an error, put the buttons in a new array
    @commands.command()
    async def setup(self, ctx):
        await ctx.send(

        # Change title to whatever you want the embed title to be
        # change the description to whatever you want the description to be
        # go on spycolor.com, search for a color, and hit ctrl-f and type "decimal"
        # then copy the numbers next to the word decimal
        embed=discord.Embed(title='Reaction Roles (Title)', description=f'**Click on a button to get your role!** (description)', color=65535),
        components=[

        # Start of Array 1 (arrays are seperated by the [ and the ])
        [Button(style=ButtonStyle.red, label="Among us", custom_id="role_1"), # button id is "role_1"
        Button(style=ButtonStyle.red, label="Apex Legends", custom_id="role_2"),
        Button(style=ButtonStyle.red, label="Roblox", custom_id="role_3"),
        Button(style=ButtonStyle.red, label="Valorant", custom_id="role_4")], # end of array 1

        # Start of Array 2
        [Button(style=ButtonStyle.green, label="Minecraft", custom_id="role_5"),
        Button(style=ButtonStyle.green, label="ARK: Survival Evo", custom_id="role_6"),
        Button(style=ButtonStyle.blue, label="Fortnite", custom_id="role_7"),
        Button(style=ButtonStyle.blue, label="Rocket League", custom_id="role_8"),
        Button(style=ButtonStyle.grey, label="CS:GO", custom_id="role_9")] # end of array 2

        ])  # This is the end of the components, do not delete this!

        while True:
            res = await self.client.wait_for("button_click", check=lambda m: m.author == ctx.author and m.channel == ctx.message.channel)

            if res.component.id == "role_1": # connects to the button "Among us" because the button id's are the same
                role = get(res.guild.roles, name='Among us') # name of the you want to give
                user = res.guild.get_member(res.author.id) # getting the user
                await user.add_roles(role) # adding the role to the user
                await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{role.mention} added!") # the popup after clicking the button
            
            
            if res.component.id == "role_2": # connects to the button "Apex Legends" because the button id's are the same
                role = get(res.guild.roles, name='Apex Legends') # name of the role you want to give
                user = res.guild.get_member(res.author.id) # getting the user
                await user.add_roles(role) # adding the role to the user
                await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{role.mention} added!") # the popup after clicking the button
            
            
            if res.component.id == "role_3":
                role = get(res.guild.roles, name='Roblox')
                user = res.guild.get_member(res.author.id)
                await user.add_roles(role)
                await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{role.mention} added!")


            if res.component.id == "role_4":
                role = get(res.guild.roles, name='Valorant')
                user = res.guild.get_member(res.author.id)
                await user.add_roles(role)
                await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{role.mention} added!")


            if res.component.id == "role_5":
                role = get(res.guild.roles, name='Minecraft')
                user = res.guild.get_member(res.author.id)
                await user.add_roles(role)
                await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{role.mention} added!")


            if res.component.id == "role_6":
                role = get(res.guild.roles, name='ARK: Survival Evo')
                user = res.guild.get_member(res.author.id)
                await user.add_roles(role)
                await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{role.mention} added!")


            if res.component.id == "role_7":
                role = get(res.guild.roles, name='Fortnite')
                user = res.guild.get_member(res.author.id)
                await user.add_roles(role)
                await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{role.mention} added!")


            if res.component.id == "role_8":
                role = get(res.guild.roles, name='Rocket League')
                user = res.guild.get_member(res.author.id)
                await user.add_roles(role)
                await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{role.mention} added!")


            if res.component.id == "role_9":
                role = get(res.guild.roles, name='CS:GO')
                user = res.guild.get_member(res.author.id)
                await user.add_roles(role)
                await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{role.mention} added!")




def setup(client):
    client.add_cog(Roles(client))
