from data.ETL.etl import Etl
from visualization.display import printGrapgh

def main():
    etl1 = Etl("hej","msft")

    df = etl1._get()
    df = etl1.transform()
    #print(df[:])
    #printGrapgh(df)
    print(df)
if __name__ == "__main__":
    main()