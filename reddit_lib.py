import os
import random
import praw
from utils.color_logger import *

logger = colorlog.getLogger("reddit")


class RedditLib:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.getenv('client_id'),
            client_secret=os.getenv('reddit_token'),
            user_agent='Discord Trollbot',
            redirect_uri=os.getenv('redir_url'),
            over_18='True',
            over18='True',
            nsfw='True'
        )

    def get_nsfw_gif(self, chosen_subreddit):
        # reddit.random_subreddit(True)  # True for NSFW
        logger.info(f"Chosen Subreddit: {chosen_subreddit}")
        try:
            image_urls = []
            # for submission in reddit.subreddit(chosen_subreddit).stream.submissions():
            for submission in self.reddit.subreddit(chosen_subreddit).hot(limit=50):
                # logger.info(f'Submission: {submission}')
                # logger.info(f"submission url: {submission.url}")
                image_urls.append(submission.url)
                # TODO Add only this type of submissions?
                logger.info(f"submission media: {submission.media}")
                logger.info(f"submission media_embed: {submission.media_embed}")
            # logger.info(f"Appended urls {image_urls}")
            discord_receive = image_urls[random.randint(0, len(image_urls) - 1)]
            return discord_receive

        except Exception as e:
            logger.info(f"Exception caught: \n{e}")
            return "This sub is either banned, quarantined, or does not exist."

    def search_nsfw_reddit(self, chosen_term):
        # reddit.random_subreddit(True)  # True for NSFW
        logger.info(f"Chosen term: {chosen_term}")
        try:
            image_urls = []
            for submission in self.reddit.subreddit('all').search(chosen_term, limit=50, params={'include_over_18': 'on'}):
                if submission.media:
                    image_urls.append(submission.url)
                    # logger.info(f"submission url: {submission.url}")

                logger.info(f"submission media: {submission.media}")
                logger.info(f"submission media_embed: {submission.media_embed}")

            logger.info(f"Appended urls {image_urls}")
            if len(image_urls) > 0:
                discord_receive = image_urls[random.randint(0, len(image_urls) - 1)]
            else:
                discord_receive = 'No he encontrao na :('
            return discord_receive

        except Exception as e:
            logger.info(f"Exception caught: \n{e}")
            return "This sub is either banned, quarantined, or does not exist."
