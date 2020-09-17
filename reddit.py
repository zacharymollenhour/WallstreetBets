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

#Main
def main():

    stocks_list = []


    #Read in tickers
    with open('companylist.csv','r') as w:
        stocks = w.readlines()

        for a in stocks:
            a = a.replace('\n','')
            stocks_list.append(a)
            single_stock_earnings = get_stockdata(a)
            print(single_stock_earnings)
    df = pd.DataFrame(single_stock_earnings)
    print(df)
    #Reddit API Credentials
    reddit = praw.Reddit(client_id='4Em1CElJRKZetA',
                        client_secret='bPQUDPLovSzPtVj5t71gRV9DCGc',
                        user_agent='stock')

    #Subreddit Information
    subreddit = reddit.subreddit('wallstreetbets')
    submission = reddit.submission(id="it5xpg")
    submission.comment_sort = 'new'
    tickercounter_dict = { "ticker": []}
    #Dictionary to store response data
    topics_dict = { "body":[],
                    "created": []}

    #filter through the comments
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        topics_dict["body"].append(top_level_comment.body.encode("utf-8"))
        topics_dict["created"].append(dt.datetime.fromtimestamp(top_level_comment.created))
        for a in stocks_list:
            #print(quandl.get("XNYS/AAPL"))
            if(a in top_level_comment.body):
                tickercounter_dict["ticker"].append(a)

    #Store in dataframe
    topics_data = pd.DataFrame(topics_dict)
    mentionedtickers = pd.DataFrame(tickercounter_dict)


def get_date(created):
    return dt.datetime.fromtimestamp(created)


#retrieve stock data
def get_stockdata(ticker):
    basepath = 'https://cloud.iexapis.com/stable/stock/'
    basepath2 = '/quote?token=pk_04da3e6c36334468ac1513b3adfe1531'
    url = basepath + ticker + basepath2
    x = requests.get(url)
    price = x.text
    #print(price)
    return price

main()