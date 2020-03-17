import os
# Discord imports
import discord
from discord.ext import commands
import requests
# External libraries
import js2py
import random
from Naked.toolshed.shell import execute_js
from lxml import etree
from io import StringIO
# Logger library
from utils.color_logger import *

# promise
from promise import Promise, promise

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
async def porn(ctx):

    """
    Source Js2Py: https://github.com/PiotrDabkowski/Js2Py
    Source Pornsearch: https://github.com/LucasLeandro1204/Pornsearch
    Returns ¿gif???
    -------
    """
    query = 'porn'
    page = '1'
    url = 'http://www.sex.com/search/gifs?query='+query+'&page='+page
    r = requests.get(url=url)
    html = r.content.decode("utf-8")

    # Create your etree with a StringIO object which functions similarly
    # to a fileHandler
    tree = etree.parse(StringIO(html), parser=parser)

    # Call this function and pass in your tree
    def get_links(tree):
        # This will get the anchor tags <a href...>
        refs = tree.xpath("//a")
        # Get the url from the ref
        links = [link.get('href', '') for link in refs]
        # Return a list that only ends with .com.br
        return [l for l in links if l.endswith('.com.br')]

    # Example call
    links = get_links(tree)
    logger.info(f"{r.status_code}{r.content}")
    await ctx.send('Pero que tonto eres!')


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

Pornsearch = js2py.require('pornsearch')
# token = os.getenv('token')
token = 'MTc1NTE4NDA3ODg4ODYzMjMy.XnEKEA.BhuPxdOS5pqTSu-WjeQIggT__Y0'
bot.run(token)
