import os

import colorlog
from praw import reddit
import praw

from requests import Session

logger = colorlog.getLogger("reddit")

def get_nsfw_gif():
    reddit.read_only = True
    # r = praw.Reddit(
    #     user_agent="<Discord>:<trollbot>:<1.0> (by /u/DiEVeXx)",
    #     client_id=os.getenv('client_id'),
    #     client_secret=os.getenv('reddit_token'),
    #     # redirect_uri=os.getenv('redirect_ui')
    # )
    r = praw.Reddit(
        client_id=os.getenv('client_id'),
        client_secret=os.getenv('reddit_token'),
        user_agent='Discord Trollbot')
    # sub = r.subreddit("NSFW_GIF")
    # continued from code above

    for submission in r.subreddit('learnpython').hot(limit=10):
        print(submission.title)

    # Output: 10 submissions
    # posts = sub.hot(limit=100)
#
    # vids = []
    # logger = colorlog.getLogger("reddit nsfw_gif")
#
    # for p in posts:
    #     try:
    #         url = p.media['reddit_media']['fallback_url']
    #         url = url.split("?")[0]
    #         name = p.title[:30].rstrip() + ".mp4"
    #         vids.append((url, name))
    #     except:
    #         pass

    #logger.info("found {}".format(len(vids)))
    return
