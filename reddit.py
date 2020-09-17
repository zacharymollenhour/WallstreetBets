import praw
import pandas as pd
import datetime as dt
from praw.models import MoreComments

#Main
def main():

    #Reddit API Credentials
    reddit = praw.Reddit(client_id='4Em1CElJRKZetA',
                        client_secret='bPQUDPLovSzPtVj5t71gRV9DCGc',
                        user_agent='stock')

    #Subreddit Information
    subreddit = reddit.subreddit('wallstreetbets')
    submission = reddit.submission(id="it5xpg")
    submission.comment_sort = 'new'

    #Dictionary to store response data
    topics_dict = { "body":[],
                    "created": []}

    #filter through the comments
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        topics_dict["body"].append(top_level_comment.body.encode("utf-8"))
        topics_dict["created"].append(dt.datetime.fromtimestamp(top_level_comment.created))

    #Store in dataframe
    topics_data = pd.DataFrame(topics_dict)
    

def get_date(created):
    return dt.datetime.fromtimestamp(created)

main()