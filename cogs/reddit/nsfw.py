import random
import discord
import discord.ext.commands as commands

from cogs.reddit.nsfw_subreddits import choose_nsfw_subreddits
from cogs.reddit.reddit_lib import RedditLib
from utils.color_logger import *
logger = colorlog.getLogger("NSFW")


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
    porn_subreddits = RedditLib().search_media_subreddit(query)
    # elegir un subreddit random de la lista de subreddits
    choice = porn_subreddits[random.randint(0, len(porn_subreddits) - 1)]
    return choice


def choose_pornsite(query: str):
    query = query.lower()
    porn_subreddits = choose_nsfw_subreddits(query)
    # elegir un subreddit random de la lista de subreddits
    random_choice = porn_subreddits[random.randint(0, len(porn_subreddits) - 1)]
    return random_choice


def find_porn(chosen_subreddit='NSFW_GIF'):
    return RedditLib().get_media_url_subreddit(chosen_subreddit)
    # return ""


def search_porn(query='porn'):
    """"""
    choice = choose_pornsite(query)
    return find_porn(choice)


class Nsfw(commands.Cog):
    """😏🔞"""

    def __init__(self, bot):
        self.bot = bot

    def cog_unload(self):
        """Handles special unloading."""

    def cog_check(self, ctx):
        """Extra checks for the cog's commands."""
        if not ctx.guild:
            raise commands.NoPrivateMessage('This command cannot be used in a private message.')
        return True

    async def cog_command_error(self, ctx, error):
        """Error handler for the cog's commands."""
        if not isinstance(error, (commands.UserInputError, commands.CheckFailure)):
            raise error
        try:
            await ctx.send(error)
        except discord.Forbidden:
            pass  # /shrug

# ---------------------------------------------------NSFW COMMANDS------------------------------------------------------
    @commands.command()
    async def webcam(self, ctx):
        """finds nsfw webcam post in subreddits"""
        await ctx.message.add_reaction('✅')
        return await ctx.send(search_porn('webcam'))

    @commands.command()
    async def facial(self, ctx):
        """finds nsfw facial post in subreddits"""
        await ctx.message.add_reaction('✅')
        return await ctx.send(search_porn('facial'))

    @commands.command()
    async def squirt(self, ctx):
        """finds nsfw squirt post in subreddits"""
        await ctx.message.add_reaction('✅')
        return await ctx.send(search_porn('squirt'))

    @commands.command()
    async def cosplay(self, ctx):
        """finds nsfw cosplayers post in subreddits"""
        await ctx.message.add_reaction('✅')
        return await ctx.send(search_porn('cosplay'))

    @commands.command()
    async def boobies(self, ctx):
        """finds nsfw boobies post in subreddits"""
        await ctx.message.add_reaction('✅')
        return await ctx.send(search_porn('boobies'))

    @commands.command()
    async def hentai(self, ctx):
        """finds nsfw hentai post in subreddits"""
        await ctx.message.add_reaction('✅')
        return await ctx.send(search_porn('hentai'))

    @commands.command()
    async def anal(self, ctx):
        """finds nsfw anal post in subreddits"""
        await ctx.message.add_reaction('✅')
        return await ctx.send(search_porn('anal'))

    @commands.command()
    async def fap(self, ctx):
        """finds nsfw gaming post in subreddits"""
        await ctx.message.add_reaction('✅')
        return await ctx.send(search_porn('fap'))

    @commands.command()
    async def hardcore(self, ctx):
        """finds nsfw hardcore post in subreddits"""
        await ctx.message.add_reaction('✅')
        return await ctx.send(search_porn('hardcore'))

    @commands.command()
    async def blowjob(self, ctx):
        """finds nsfw blowjob post in subreddits"""
        await ctx.message.add_reaction('✅')
        return await ctx.send(search_porn('blowjob'))

    @commands.command()
    async def wtf(self, ctx):
        """finds nsfw wtf post in subreddits"""
        await ctx.message.add_reaction('✅')
        return await ctx.send(search_porn('wtf'))

    @commands.command()
    async def pornstar(self, ctx):
        """finds nsfw pornstars post in subreddits"""
        await ctx.message.add_reaction('✅')
        return await ctx.send(search_porn('pornstar'))

    @commands.command()
    async def nudes(self, ctx):
        """finds nsfw nudes post in subreddits"""
        await ctx.message.add_reaction('✅')
        return await ctx.send(search_porn('nudes'))

    @commands.command()
    async def milf(self, ctx):
        """finds nsfw nudes post in subreddits"""
        await ctx.message.add_reaction('✅')
        return await ctx.send(search_porn('milf'))

    @commands.command()
    async def porn(self, ctx, query='porn'):
        """finds nsfw porn post in subreddits"""
        await ctx.message.add_reaction('✅')
        if query != 'porn':
            return await ctx.send(search_term(query))
        emoji1 = discord.utils.get(ctx.guild.emojis, name='ahh')
        emoji2 = discord.utils.get(ctx.guild.emojis, name='booty')
        msg = await ctx.send(search_porn(query))
        await msg.add_reaction(emoji2)
        return await msg.add_reaction(emoji1)

        # from discord import guild
        # return await ctx.message.add_reaction(emoji='<:ahh:>')


