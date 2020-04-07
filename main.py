import asyncio
import os
import random

import discord
from discord.ext import commands
from nsfw_subreddits import choose_porn_subreddits, nsfw_subreddits
from reddit_lib import RedditLib
from utils.color_logger import *
from music2 import Music

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


@client.event
async def on_message(message):
    if message.content.startswith('$thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')


@bot.event
async def on_member_join(member):
    logger.info(f"new member in server {member}")
    guild = member.guild
    file = discord.File('./images/mirahijo.png')
    if guild.system_channel is not None:
        await guild.system_channel.send(f"Mira Ramón!"+'\t'*6+"{member.mention}")
        await guild.system_channel.send(file=file)
        await guild.system_channel.send("Otro mongolito!")
        # ret_str = str("""```css\nOtro mongolito!```""")
        # embed = discord.Embed(title="Mira ramón!")
        # embed.add_field(name="\t\t\t\t\t\t\t\t"+member.mention, value=ret_str)
        # await guild.system_channel.send(embed=embed, file=file)


# ---------------------------------------------------NSFW COMMANDS------------------------------------------------------
@bot.command()
async def webcam(ctx):
    """finds nsfw webcam post in subreddits"""
    await ctx.message.add_reaction('✅')
    return await ctx.send(search_porn('webcam'))


@bot.command()
async def facial(ctx):
    """finds nsfw facial post in subreddits"""
    await ctx.message.add_reaction('✅')
    return await ctx.send(search_porn('facial'))


@bot.command()
async def squirt(ctx):
    """finds nsfw squirt post in subreddits"""
    await ctx.message.add_reaction('✅')
    return await ctx.send(search_porn('squirt'))


@bot.command()
async def cosplay(ctx):
    """finds nsfw cosplayers post in subreddits"""
    await ctx.message.add_reaction('✅')
    return await ctx.send(search_porn('cosplay'))


@bot.command()
async def boobies(ctx):
    """finds nsfw boobies post in subreddits"""
    await ctx.message.add_reaction('✅')
    return await ctx.send(search_porn('boobies'))


@bot.command()
async def hentai(ctx):
    """finds nsfw hentai post in subreddits"""
    await ctx.message.add_reaction('✅')
    return await ctx.send(search_porn('hentai'))


@bot.command()
async def anal(ctx):
    """finds nsfw anal post in subreddits"""
    await ctx.message.add_reaction('✅')
    return await ctx.send(search_porn('anal'))


@bot.command()
async def fap(ctx):
    """finds nsfw gaming post in subreddits"""
    await ctx.message.add_reaction('✅')
    return await ctx.send(search_porn('fap'))


@bot.command()
async def hardcore(ctx):
    """finds nsfw hardcore post in subreddits"""
    await ctx.message.add_reaction('✅')
    return await ctx.send(search_porn('hardcore'))


@bot.command()
async def blowjob(ctx):
    """finds nsfw blowjob post in subreddits"""
    await ctx.message.add_reaction('✅')
    return await ctx.send(search_porn('blowjob'))


@bot.command()
async def wtf(ctx):
    """finds nsfw wtf post in subreddits"""
    await ctx.message.add_reaction('✅')
    return await ctx.send(search_porn('wtf'))


@bot.command()
async def porn(ctx, query='porn'):
    """finds nsfw porn post in subreddits"""
    await ctx.message.add_reaction('✅')
    if query != 'porn':
        return await ctx.send(search_term(query))
    return await ctx.send(search_porn(query))


# -------------------------------------------------NSFW AUX FUNCS-------------------------------------------------------

def search_term(query: str):
    """
    search in reddit for a query
    Parameters
    ----------
    query

    Returns
    -------

    """
    query = query.lower()
    porn_subreddits = RedditLib().search_nsfw_reddit(query)
    # elegir un subreddit random de la lista de subreddits
    choice = porn_subreddits[random.randint(0, len(porn_subreddits) - 1)]
    return choice


def choose_pornsite(query: str):
    query = query.lower()
    porn_subreddits = choose_porn_subreddits(query)
    # elegir un subreddit random de la lista de subreddits
    random_choice = porn_subreddits[random.randint(0, len(porn_subreddits) - 1)]
    return random_choice


def find_porn(chosen_subreddit='NSFW_GIF'):
    return RedditLib().get_nsfw_gif(chosen_subreddit)
    # return ""


def search_porn(query='porn'):
    """"""
    choice = choose_pornsite(query)
    return find_porn(choice)


# -------------------------------------MAIN---------------------------------------
token = os.getenv('token')
bot.add_cog(Music(bot))
bot.run(token)
