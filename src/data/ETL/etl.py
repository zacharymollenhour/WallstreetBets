from iexfinance.stocks import get_historical_data, get_historical_intraday
from datetime import datetime
import matplotlib.pyplot as plt
import requests
from data.ETL.constants import (BASE_URL,
                           CHART_RANGES,
                           RANGES,
                           DATE_FIELDS)
#Class for getting the stock data
class Etl:
    """
    Extraction, transformation and loading of data for machine learning
    """

    def __init__(self,df,ticker):
        self.df = df
        self.ticker = ticker

    #Get Function
    def _get(self, params={}):
        request_url =f"{BASE_URL}/stock/{self.ticker}/quote?token=pk_04da3e6c36334468ac1513b3adfe1531"
        response = requests.get(request_url, params=params)
        if response.status_code != 200:
            raise Exception(f"{response.status_code}: {response.content.decode('utf-8')}")
        self.df = response.json()
        return self.df

    def extract_historical(self):
        """
        Extract function to extract data and create a table to be used later in machine learning
        """
        start = datetime(2020, 6, 1)
        end = datetime(2020,9,16)

        self.df = get_historical_intraday(self.ticker, start=start,token="pk_04da3e6c36334468ac1513b3adfe1531")


        return self.df

    def transform(self):
        return self.df

    def load(self):
        print("hej")
    