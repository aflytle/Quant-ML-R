import sklearn
import os 
import pandas as pd
import matplotlib
import numpy as np
from csv_reader import Price_Data


AAPL = Price_Data("HistoricalData_1663390678621.csv")

prices = AAPL.average_list()


if __name__ == "__main__":
    matplotlib.plot([i for i in range(1,len(prices))],prices)

