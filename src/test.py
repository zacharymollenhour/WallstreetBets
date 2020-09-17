from data.ETL.etl import Etl
from visualization.display import printGrapgh
from reddit import main
import praw
import pandas as pd
import datetime as dt
from praw.models import MoreComments
from rtstock.stock import Stock
from collections import Counter
from yahoo_fin import stock_info as si
import json
import requests
import quandl
def main():
    stocks_list = []
    live_data = []

    #Reddit API Credentials
    reddit = praw.Reddit(client_id='4Em1CElJRKZetA',
                        client_secret='bPQUDPLovSzPtVj5t71gRV9DCGc',
                        user_agent='stock')

    #Subreddit Information
    subreddit = reddit.subreddit('wallstreetbets')
    submission = reddit.submission(id="iugmeq")
    submission.comment_sort = 'new'
    tickercounter_dict = { "ticker": []}
    with open('companylist.csv','r') as w:
        stocks = w.readlines()
        for row in stocks:
            row = row.replace('\n','')
            stocks_list.append(row)
    #Dictionary to store response data
    topics_dict = { "body":[],
                    "created": []}
    single_stock_earnings = []
    etl = []
    #filter through the comments
    i = 0
    etl1 = Etl("test1","test")
    
    response = etl1._getMovers()
    for i in response:
        print(i)
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        topics_dict["body"].append(top_level_comment.body.encode("utf-8"))
        topics_dict["created"].append(dt.datetime.fromtimestamp(top_level_comment.created))
        for a in stocks_list:
            if(a in top_level_comment.body):
                #print(a)
                tickercounter_dict["ticker"].append(a)
                etl.append(Etl(a,a))
    etl = list(dict.fromkeys(etl))
    """ for items in etl:
        result = items._get()
        print(result) """




        #print(live_data)
if __name__ == "__main__":
    main()