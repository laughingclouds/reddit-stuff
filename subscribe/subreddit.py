from configparser import ConfigParser

from praw import reddit
from utils.models import sub


def subscribeSub(subreddit: sub):
    """Subscribe to the given subreddit"""
    subreddit.subscribe()