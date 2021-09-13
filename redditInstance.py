"""
Creating a reddit instance here, to be used in other modules. Also initializing
any other variables that might be needed.
"""
from configparser import ConfigParser
from typing import Union

import praw
from praw.models.helpers import SubredditHelper
from praw.reddit import Subreddit

cfg = ConfigParser()
cfg.read('config.cfg')

reddit = praw.Reddit(
    client_id = cfg['DEFAULT']['client_id'],
    client_secret = cfg['DEFAULT']['client_secret'],
    user_agent = cfg['DEFAULT']['user_agent'],
    username = cfg['OAuth']['username'],
    password = cfg['OAuth']['password'],
)

subreddit: Union[SubredditHelper, Subreddit] = reddit.subreddit(cfg['Sub']['name'])