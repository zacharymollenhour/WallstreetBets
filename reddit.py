import praw
import pandas as pd
import datetime as dt
from praw.models import MoreComments
from rtstock.stock import Stock
from collections import Counter
#Main
def main():
    stocks_list = []
    #Read in tickers
    with open('companylist.csv','r') as w:
        stocks = w.readlines()
        for a in stocks:
            a = a.replace('\n','')
            stocks_list.append(a)
        #print(stocks_list)
    #print(stock_tickers['Symbol'])

    #Reddit API Credentials
    reddit = praw.Reddit(client_id='4Em1CElJRKZetA',
                        client_secret='bPQUDPLovSzPtVj5t71gRV9DCGc',
                        user_agent='stock')

    #Subreddit Information
    subreddit = reddit.subreddit('wallstreetbets')
    submission = reddit.submission(id="it5xpg")
    submission.comment_sort = 'new'
    tickercounter_dict = { "ticker": [],
                            "counter":[]}
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
    stock_dict = Counter()
    start = 2

    #Search for tickers in reddit comments
    for a in stocks_list:
        #print(a)
        if(topics_data['body'].astype(str).str.contains(a,start).any()):
            topics_data["Indexes"] = topics_data['body'].astype(str).str.find(a,start)
            tickercounter_dict["ticker"].append(a)
            tickercounter_dict["counter"].append(topics_data['body'])

    #print(tickercounter_dict)
    #print(stock_dict[ticker])
def get_date(created):
    return dt.datetime.fromtimestamp(created)

main()