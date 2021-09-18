from typing import Union

from praw.reddit import Subreddit
from praw.models.helpers import SubredditHelper

sub: Union[SubredditHelper, Subreddit]
dictStr: dict[str, str]
listDictStr: list[dict[str, str]]
