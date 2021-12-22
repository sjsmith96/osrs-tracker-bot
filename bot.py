import os
import random

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!')


@bot.command(name='greeting')
async def greet(ctx):
    await ctx.send('Hello!')

@bot.command(name='day')
async def delta_day(ctx, player):
    await ctx.send(f'You want the day changes for: {player}. Not implement yet!')

@bot.command(name='week')
async def delta_day(ctx, player):
    await ctx.send(f'You want the week changes for: {player}. Not implement yet!')

@bot.command(name='month')
async def delta_day(ctx, player):
    await ctx.send(f'You want the month changes for: {player}. Not implement yet!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)



