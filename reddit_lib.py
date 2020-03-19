import colorlog
import discord
import praw
import random
import os
import urllib.request as req
import time
from utils.color_logger import *

logger = colorlog.getLogger("reddit")
import logging


def get_nsfw_gif(chosen_subreddit):
    reddit = praw.Reddit(
        client_id=os.getenv('client_id'),
        client_secret=os.getenv('reddit_token'),
        user_agent='Discord Trollbot',
        redirect_uri=os.getenv('redir_url'),
        over_18='True',
        over18='True',
        nsfw='True'
    )
    # reddit.random_subreddit(True)  # True for NSFW
    logger.info(f"Chosen Subreddit: {chosen_subreddit}")
    try:
        image_urls = []
        i = 0
        # for submission in reddit.subreddit(chosen_subreddit).stream.submissions():
        for submission in reddit.subreddit(chosen_subreddit).hot(limit=200):
            # logger.info(f'Submission: {submission}')
            # logger.info(f"submission url: {submission.url}")
            image_urls.append(submission.url)
        # logger.info(f"Appended urls {image_urls}")
        discord_receive = image_urls[random.randint(0, len(image_urls) - 1)]
        return discord_receive

    except Exception as e:
        logger.info(f"Exception caught: \n{e}")
        return "This sub is either banned, quarantined, or does not exist."
