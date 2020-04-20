import asyncio
import os
import discord
from discord.ext import commands
from cogs.reddit.nsfw import Nsfw
from utils.color_logger import *
from cogs.music.music import Music

logger = colorlog.getLogger("Main")
client = discord.Client()
token = os.getenv('token')
logger.info("-" * 40 + "Discord Envs" + "-" * 40)
logger.info(f"token {token}")
logger.info("-" * 40 + "Reddit Envs" + "-" * 40)
logger.info(f"{os.getenv('client_id')}")
logger.info(f"{os.getenv('reddit_token')}")
logger.info(f"{os.getenv('redir_url')}")
logger.info("-" * 90)
logger = colorlog.getLogger("Main")

description = \
    '''A simple bot based on Rapptz/discord.py with some NSFW utilities 😜 and improved music! 🎵\nGithub: 
    DiEVeXx/discord.py '''
bot = commands.Bot(command_prefix='pls ', description=description)


@bot.event
async def on_ready():
    logger.info('-' * 90)
    logger.info('My name is {} and my user id is {}.\tSTATE:WORKING'.format(bot.user.name, bot.user.id))
    logger.info('-' * 90)


# Not Working Currently
@client.event
async def on_message(message):
    if message.content.startswith('thumb'):
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

# -------------------------------------MAIN---------------------------------------
token = os.getenv('token')
bot.add_cog(Music(bot))
bot.add_cog(Nsfw(bot))
bot.run(token)
