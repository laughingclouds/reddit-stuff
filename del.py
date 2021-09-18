"""
NOTE: It would be nice if `GallerySubmit` also returns the link(s) to the post it submitted to.
In fact if every other submission related module does this it would be nice.
"""
from gallerysubmit import gallerySubmit, subNames

from utils.models import sub
from utils.redditInstance import reddit

subreddit: sub = reddit.subreddit(subNames[0])

gallerySubmit(subreddit)
