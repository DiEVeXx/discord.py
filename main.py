from discord.ext import commands
from nsfw_subreddits import choose_porn_subreddits
from utils.color_logger import *
import discord
import praw
import random
import os
import urllib.request as req
import time
from utils.color_logger import *
from reddit_lib import get_nsfw_gif

logger = colorlog.getLogger("Main")
client = discord.Client()
token = os.getenv('token')
logger.info("-" * 15 + "Discord Envs" + "-" * 15)
logger.info(f"token {token}")
logger.info("-" * 15 + "Reddit Envs" + "-" * 15)
logger.info(f"{os.getenv('client_id')}")
logger.info(f"{os.getenv('reddit_token')}")
logger.info(f"{os.getenv('redir_url')}")
logger.info("-" * 41)

logger = colorlog.getLogger("Main")

description = \
    '''An example bot to showcase the discord.ext.commands extension module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='pls ', description=description)


@bot.event
async def on_ready():
    logger.info('-' * 45)
    logger.info('My name is {} and my user id is {}. STATE:WORKING'.format(bot.user.name, bot.user.id))
    logger.info('-' * 45)


@bot.command()
async def cosplay(ctx, query='cosplay'):
    return await ctx.send(search_porn(ctx, query))


@bot.command()
async def hentai(ctx, query='hentai'):
    return await ctx.send(search_porn(ctx, query))


@bot.command()
async def anal(ctx, query='anal'):
    return await ctx.send(search_porn(ctx, query))


@bot.command()
async def fap(ctx, query='fap'):
    return await ctx.send(search_porn(ctx, query))


@bot.command()
async def hardcore(ctx, query='hardcore'):
    return await ctx.send(search_porn(ctx, query))


@bot.command()
async def porn(ctx, query='porn'):
    return await ctx.send(search_porn(ctx, query))
# --------------------------------------------------------------------------------


def choose_pornsite(query: str):
    query = query.lower()
    porn_subreddits = choose_porn_subreddits(query)
    # elegir un subreddit random de la lista de subreddits
    choice = porn_subreddits[random.randint(0, len(porn_subreddits) - 1)]
    return choice


# @bot.command()
def search_porn(ctx, query='porn'):
    choice = choose_pornsite(query)
    resp = None
    try:
        if choice:
            resp = find_porn(ctx, choice)
        if resp is not None:
            return resp
        else:
            return "No se ha encontrado nada"

    except Exception as e:
        logger.error("Exception produced: \n{}".format(e))
        return "He petao :scream:"


def find_porn(ctx, chosen_subreddit='NSFW_GIF'):
    return get_nsfw_gif(chosen_subreddit)
    # return ""


# SOME BOT COMMAND EXAMPLES
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


#
#
# @bot.command()
# async def roll(ctx, dice: str):
#     """Rolls a dice in NdN format."""
#     try:
#         rolls, limit = map(int, dice.split('d'))
#     except Exception:
#         await ctx.send('Format has to be in NdN!')
#         return
#
#     result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
#     await ctx.send(result)
#
#
# @bot.command(description='For when you wanna settle the score some other way')
# async def choose(ctx, *choices: str):
#     """Chooses between multiple choices."""
#     await ctx.send(random.choice(choices))
#
#
# @bot.command()
# async def repeat(ctx, times: int, content='repeating...'):
#     """Repeats a message multiple times."""
#     for i in range(times):
#         await ctx.send(content)
#
#
# @bot.command()
# async def joined(ctx, member: discord.Member):
#     """Says when a member joined."""
#     await ctx.send('{0.name} joined in {0.joined_at}'.format(member))
#
#
# @bot.group()
# async def cool(ctx):
#     """Says if a user is cool.
#
#     In reality this just checks if a subcommand is being invoked.
#     """
#     if ctx.invoked_subcommand is None:
#         await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))
#
#
# @cool.command(name='bot')
# async def _bot(ctx):
#     """Is the bot cool?"""
#     await ctx.send('Yes, the bot is cool.')

token = os.getenv('token')
bot.run(token)
