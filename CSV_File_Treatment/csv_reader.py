import os
import sys
import numpy
import pandas as pd

class Price_Data:

    def __init__(self, file):
        self.data = pd.read_csv(file)

    def average_day(self,date):
        return(float(self.data[date,-1][1:]) + float(self.data[date,-2][1:]) + float(self.data[date,-3][1:]))/3

    def average_list(self):
        dailies = []
        for i in range(1,(len(self.data[1])-1)):
            dailies.append(average_day(self.data[i]))
        return(dailies)

    



    


