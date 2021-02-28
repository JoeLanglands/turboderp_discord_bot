"""The bot itself with definitions for all commands."""

import random
import time

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command(
    help="Gives the link for the bots github page so you can add stuff if you want.",
    brief="Get DK bots github page."
)
async def github(ctx):
    await ctx.send(r'Add new command suggestions or make a new branch on github: https://github.com/JoeLanglands/turboderp_discord_bot')

@bot.command(
    help="Roll for a random integer between the two given integer arguments. (Default 1-100)",
    brief="Roll a random integer."
)
async def roll(ctx, low=0, high=100):
    try:
        if high < low:
            low, high = high, low
        rand = random.randint(low, high)
        await ctx.send(f'{ctx.author.name} rolled ({low}-{high}): {rand}')
    except:
        await ctx.send('Invalid arguments try again!')

@bot.command(
    brief="Annoy everone with text-to-speech.",
    help="Annoy the shit out of everyone by sending a message as text-to-speech. (Cooldown 30 seconds)"
)
@commands.cooldown(1, 30, commands.BucketType.user)
async def tts(ctx, *args):
    await ctx.send(' '.join(args), tts=True)

@bot.command(
    alias=('DK'),
    hidden=True
)
async def dk(ctx):
    await ctx.send('Do you know what DK stands for?', tts=True)

@bot.command(
    hidden=True
)
@commands.cooldown(1, 3600, commands.BucketType.user)
async def flame(ctx, member : discord.Member):
    await ctx.send(f"{member.name} you're like the Justin Timberlake of Japan, right?", tts=True)

