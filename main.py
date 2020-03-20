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
async def webcam(ctx):
    """finds nsfw webcam post in subreddits"""
    return await ctx.send(search_porn('webcam'))


@bot.command()
async def cosplay(ctx):
    """finds nsfw cosplayers post in subreddits"""
    return await ctx.send(search_porn('cosplay'))


@bot.command()
async def boobies(ctx):
    """finds nsfw boobies post in subreddits"""
    return await ctx.send(search_porn('boobies'))


@bot.command()
async def hentai(ctx):
    """finds nsfw hentai post in subreddits"""
    return await ctx.send(search_porn('hentai'))


@bot.command()
async def anal(ctx):
    """finds nsfw anal post in subreddits"""
    return await ctx.send(search_porn('anal'))


@bot.command()
async def fap(ctx):
    """finds nsfw gaming post in subreddits"""
    return await ctx.send(search_porn('fap'))


@bot.command()
async def hardcore(ctx, query='hardcore'):
    """finds nsfw hardcore post in subreddits"""
    return await ctx.send(search_porn(query))


@bot.command()
async def blowjob(ctx, query='blowjob'):
    """finds nsfw blowjob post in subreddits"""
    return await ctx.send(search_porn(query))


@bot.command()
async def wtf(ctx, query='wtf'):
    """finds nsfw wtf post in subreddits"""
    return await ctx.send(search_porn(query))


@bot.command()
async def porn(ctx, query='porn'):
    """finds nsfw porn post in subreddits"""
    return await ctx.send(search_porn(query))


# --------------------------------------------------------------------------------


def choose_pornsite(query: str):
    query = query.lower()
    porn_subreddits = choose_porn_subreddits(query)
    # elegir un subreddit random de la lista de subreddits
    choice = porn_subreddits[random.randint(0, len(porn_subreddits) - 1)]
    return choice


def search_porn(query='porn'):
    choice = choose_pornsite(query)
    resp = None
    try:
        if choice:
            # resp = find_porn(ctx, choice)
            return find_porn(choice)
        # if resp is not None:
        #     return resp
        # else:
        #     logger.info("No he encontrado nada, buscando porno normal....")
        #     return search_porn(ctx, 'porn')
        #     # return "No se ha encontrado nada"

    except Exception as e:
        logger.error("Exception produced: \n{}".format(e))
        return "He petao :scream:"


def find_porn(chosen_subreddit='NSFW_GIF'):
    return get_nsfw_gif(chosen_subreddit)
    # return ""


# -------------------------------------MAIN---------------------------------------
token = os.getenv('token')
bot.run(token)
