"""
NOTE: It would be nice if `GallerySubmit` also returns the link(s) to the post it submitted to.
In fact if every other submission related module does this it would be nice.
"""
# from time import sleep

from time import sleep

from utils.models import sub, sbm
from gallerysubmit import gallerySubmit, subNames
from utils.redditInstance import reddit

subreddit: sub = reddit.subreddit(subNames[0])
reddit.validate_on_submit = True

submission: sbm
# for submission in subreddit.new(limit=None):
#     if not submission.approved:
#         submission.delete()

# submission = subreddit.submit(
#     "Laughing Purge",
#     """Hey folks! This is to inform ya'll that I've purged the subreddit. And I'm proud to tell you that I did NOT do that manually. I will now reply to this submission in 1 minute.""",
#     spoiler=True)

# sleep(60)
# submission.mod.approve()
submission = reddit.submission("pqtrb9")
submission.reply("It seems I couldn't query older posts. I'll get to it in the morning.")