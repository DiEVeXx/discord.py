import os

import js2py as js2py
import discord
from discord.ext import commands
import random
from Naked.toolshed.shell import execute_js


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='pls ', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def porn(ctx):
    """
    Source Js2Py: https://github.com/PiotrDabkowski/Js2Py
    Source Pornsearch: https://github.com/LucasLeandro1204/Pornsearch
    Returns ¿gif???
    -------
    """
    # USANDO LIBRERIA NAKED
    gif = execute_js('./Pornsearch/src/Pornsearch.js.search(\'porn\').gifs()')

    # USANDO js2py peta
    #PornSearch = js2py.require('pornsearch')
    #gif = execute_js(PornSearch.search('porn').gifs())
    #gif = PornSearch.gifs()
    await ctx.send(gif)
    #'const Pornsearch = require(\'pornsearch\').search(\'ass\'); \
    #Pornsearch.gifs().then(gifs => console.log(gifs));'

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
#

token = os.getenv('token')
print(token)
bot.run(token)
print('heeeelp')