import matplotlib.pyplot as plt


def printGrapgh(df):
    print(df.head())

    df.plot()
    plt.show()