"""
A reddit instance is created here, to be used in other modules. Any other 
variables that might be needed are initialized as well.
"""
from configparser import ConfigParser

import praw
from utils.models import sub

cfg = ConfigParser()
cfg.read('./config/redditInstance.cfg')

reddit = praw.Reddit(
    client_id = cfg['DEFAULT']['client_id'],
    client_secret = cfg['DEFAULT']['client_secret'],
    user_agent = cfg['DEFAULT']['user_agent'],
    username = cfg['OAuth']['username'],
    password = cfg['OAuth']['password'],
)

# subreddit: sub = reddit.subreddit(cfg['Sub']['name'])