# Discord imports
import asyncio
import os

import discord
from discord.ext import commands
# External libraries
import requests
import js2py
import random
# Logger library
from image_importer import get_images_from_url
from utils.color_logger import *

logger = colorlog.getLogger("Main")

description = \
    '''An example bot to showcase the discord.ext.commands extension module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='pls ', description=description)


@bot.event
async def on_ready():
    logger.info('-' * 10)
    logger.info('My name is {} and my user id is {}'.format(bot.user.name, bot.user.id))
    logger.info('-' * 10)


@bot.command()
async def porn(ctx, query='sex'):
    page = str(random.randint(0,10))
    video_urls = [
        #'http://www.motherless.com/term/videos/' + query + '?page=' + page,
        'http://www.pornhub.com/gifs/search?search=' + query + '&page=' + page,
        #'https://api.redtube.com/?data=redtube.Videos.searchVideos&output=json&search=' + query + '&thumbsize=big&page=' + page,
        #'http://www.sex.com/search/videos?query=' + query + '&page=' + page,
        #'https://www.xvideos.com/?k=' + query + '&p=' + page,
        #'http://www.youporn.com/search/?query=' + page + '&page=' + page
    ]

    gif_urls = [
        'http://www.sex.com/search/gifs?query='+query+'&page='+page
    ]
    imgs = get_images_from_url(video_urls[random.randint(0, len(video_urls) - 1)])
    await asyncio.sleep(1)
    if len(imgs) == 0:
        await ctx.send('No hay porno pa ti enfermito!')
    else:
        # for img in imgs:
            # logger.info(f"img contents:\n{img}")
        await ctx.send('{}\nToma enfermito!'.format(imgs[random.randint(0, len(imgs) - 1)]))


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
