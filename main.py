import pandas as pd
import numpy as np

def main():
    data = pd.read_csv("./btc.csv")
    print(data.describe())
    # print(data)


if __name__ == "__main__":
    main()