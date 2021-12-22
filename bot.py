import os
import random

import discord
from dotenv import load_dotenv

from discord.ext import commands

# OTIyOTk5MTQ1MDcyMDU0MzUy.YcJn8A.iKdYO_t_yzz5BVKQ-iYLUUYsXX0

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!')


@bot.command(name='greeting')
async def create_channel(ctx):
    await ctx.send("Hello!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)



