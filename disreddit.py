import discord
import praw
import random
import os
import urllib.request as req
import time
from utils.color_logger import *
logger = colorlog.getLogger("Main")
# import authenticate

client = discord.Client()
token = os.getenv('token')

reddit = praw.Reddit(
    client_id=os.getenv('client_id'),
    client_secret=os.getenv('reddit_token'),
    user_agent='Discord Trollbot')


@client.event
async def on_ready():
    logger.info(f'{client.user.name} is ready')
    logger.info('')


@client.event
async def on_message(message):
    toBot = {'currentTop': 'currentTop',
             'copyPasta': 'what\'s up mark?',
             'randomImage': 'randomImage',
             'cel': 'I love women'}

    username = str(message.author).split('#')[0]
    if username != str(client.user.name):
        logger.info(f'{username} entered a command:')

    start = time.time()

    if message.author == client.user:
        return

    # Links the current front page post in a particular subreddit.
    if message.content.startswith(toBot['currentTop']):
        if ' ' in message.content:
            discordSubreddit = str(message.content).split(' ')[1]

            try:
                subreddit = reddit.subreddit(discordSubreddit)

                for submission in subreddit.hot(limit=5):
                    if not submission.stickied:
                        discordReceive = {'title': submission.title,
                                          'link': f'https:/www.reddit.com{submission.permalink}'}
                        discordReceive = discordReceive['title'] + '\n' + discordReceive['link']
                        await message.channel.send(discordReceive)
                        break

            except Exception as e:
                logger.info(e)
                await message.channel.send('This sub is either banned, quarantined, or does not exist.')

    # Mark says a random copypasta.
    if message.content.lower() == toBot['copyPasta']:
        subreddit = reddit.subreddit('copypasta')

        copyPastas = []
        for submission in subreddit.hot(limit=200):
            try:
                copyPastas.append(submission.selftext)

            except:
                continue

        # Loop for when the post is too long to send to the discord channel.
        while True:
            try:
                discordReceive = copyPastas[random.randint(0, len(copyPastas) - 1)]
                await message.channel.send(discordReceive)

                break
            except:
                continue

    # Sends random image from a subreddit.
    if message.content.startswith(toBot['randomImage']):
        if ' ' in message.content:
            discordSubreddit = str(message.content).split(' ')[1]

            try:
                subreddit = reddit.subreddit(discordSubreddit)

                imageUrls = []
                for submission in subreddit.hot(limit=100):
                    if submission.url.endswith('.jpg') or submission.url.endswith('.png'):
                        imageUrls.append(submission.url)

                discordReceive = imageUrls[random.randint(0, len(imageUrls) - 1)]
                req.urlretrieve(discordReceive, 'tempDiscord.jpg')
                fullPath = os.path.join(os.getcwd(), 'tempDiscord.jpg')

                file = discord.File(fullPath)
                await message.channel.send(file=file)

                os.remove('tempDiscord.jpg')

            except Exception as e:
                logger.info(e)
                await message.channel.send('This sub is either banned, quarantined, or does not exist.')

    # Shortcels titles.
    if message.content.lower() == toBot['cel']:
        subreddit = reddit.subreddit('shortcels')

        brainPosts = []
        for submission in subreddit.hot(limit=200):
            try:
                if submission.is_self:
                    brainPosts.append(submission.selftext)
            except:
                continue

        while True:
            try:
                discordReceive = brainPosts[random.randint(0, len(brainPosts) - 1)]
                await message.channel.send(discordReceive)
                break
            except:
                continue

    try:
        for i in discordReceive.splitlines():
            logger.info('\t' + i)
    except:
        pass

    logger.info('\n\t' + f'Run time: {time.time() - start} seconds')
    logger.info('')


client.run(token)
