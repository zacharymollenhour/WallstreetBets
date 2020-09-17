from data.ETL.etl import Etl
from visualization.display import printGrapgh

def main():
    stocks_list = []
    with open('companylist.csv','r') as w:
        stocks = w.readlines()

        for a in stocks:
            a = a.replace('\n','')
            stocks_list.append(a)
            etl1 = Etl("hej",a)
            df = etl1._get()
            df = etl1.transform()
            print(df)
if __name__ == "__main__":
    main()