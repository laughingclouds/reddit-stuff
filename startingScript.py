"""
Currently working on the feature to post multiple images from a any folder
in a specific sub. We will use the function `submit_gallery()` for this purpose.
"""
from redditInstance import *
from getListImages import getListImages


images = getListImages(cfg['Gallery']['path'])

# for submission in subreddit.hot(limit=10):
#     print(submission.title)

subreddit.submit_gallery(cfg['Gallery']['title'], images)
