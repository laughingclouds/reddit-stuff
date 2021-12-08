"""
A reddit instance is created here, to be used in other modules. Any other 
variables that might be needed are initialized as well.
"""
from configparser import ConfigParser

import praw
from utils.models import sub
from utils.configworker import getSectionKeyList

__cfg = ConfigParser()
__cfg.read('./config/redditInstance.cfg')

reddit = praw.Reddit(
    client_id = __cfg['DEFAULT']['client_id'],
    client_secret = __cfg['DEFAULT']['client_secret'],
    user_agent = __cfg['DEFAULT']['user_agent'],
    username = __cfg['OAuth']['username'],
    password = __cfg['OAuth']['password'],
)

subNames = getSectionKeyList(__cfg, "Sub")
# subreddit: sub = reddit.subreddit(cfg['Sub']['name'])