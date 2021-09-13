from typing import Union
from configparser import ConfigParser

import praw
from praw.models.helpers import SubredditHelper
from praw.models import Submission
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

subreddit: Union[SubredditHelper, Subreddit] = reddit.subreddit(cfg['Sub']['name2'])

submission: Submission # type annotating
for submission in subreddit.new(limit=1):
    print(submission.id)

print('\n\n')

for submission in subreddit.hot(limit=1):
    print(submission.title)
