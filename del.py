"""
NOTE: It would be nice if `GallerySubmit` also returns the link(s) to the post it submitted to.
In fact if every other submission related module does this it would be nice.
"""
# from time import sleep
from utils.models import sub, sbm, com
from utils.redditInstance import reddit, subNames

subreddit: sub = reddit.subreddit(subNames[2])
reddit.validate_on_submit = True

submission: sbm
mention: com
# for submission in subreddit.new(limit=None):
#     if not submission.approved:
#         submission.delete()

# submission = subreddit.submit(
#     "Laughing Purge",
#     """Hey folks! This is to inform ya'll that I've purged the subreddit. And I'm proud to tell you that I did NOT do that manually. I will now reply to this submission in 1 minute.""",
#     spoiler=True)

# submission.mod.approve()
# print("Approved")
# submission = reddit.submission("pv3w1b")
# submission.reply("It seems I couldn't query older posts. I'll get to it in the morning.")

while True:
    for mention in reddit.inbox.mentions(limit=None):
        print(mention.author)
        mention.reply("What up? You want something?")