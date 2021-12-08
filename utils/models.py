from typing import Union
from praw.models.reddit.comment import Comment

from praw.reddit import Subreddit, Submission
from praw.models.helpers import SubredditHelper

# PRAW custom types
sub = Union[SubredditHelper, Subreddit]
sbm = Submission
com = Comment

# Python custom types
dictStr = dict[str, str]
listDictStr = list[dict[str, str]]
