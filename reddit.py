import praw
import pandas as pandas
import datetime as dt
from praw.models import MoreComments

reddit = praw.Reddit(client_id='4Em1CElJRKZetA',
                     client_secret='bPQUDPLovSzPtVj5t71gRV9DCGc',
                     user_agent='stock')

subreddit = reddit.subreddit('wallstreetbets')
submission = reddit.submission(id="iu3i05")

topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \ 
                "comms_num": [], \
                "created": [], \
                "body":[]}


for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body.encode("utf-8"))

