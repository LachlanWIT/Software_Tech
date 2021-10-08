import wx
import wx.grid
import pandas as pd
from matplotlib import pyplot as plt
import datetime
from numpy.core.defchararray import lower

# LOAD THE DATA NEEDED
data = pd.read_csv('penalty_data_set_2.csv', low_memory=False)

# GLOBAL VARIABLES
start_date = datetime.date(2014, 1, 1)
end_date = datetime.date(2016, 1, 1)


# FUNCTIONS TO RETRIEVE LISTINGS BASED ON USER INPUTS
#def PenaltyCases(listingToDisplay):



#def findKeyword(startperiod, endperiod, keyword):



#def getListings(startperiod, endperiod, suburbName='sydney', keyword=None):




def CamVsRadar(start_date, end_date, checkboxvalue):
        camera = (data[data.stack().str.contains("Camera Detected").any(level=0)])
        radar = (data[data.stack().str.contains("Radar").any(level=0)])
        for row in camera:
            if camera["OFFENCE_MONTH"] >= start_date and camera["OFFENCE_MONTH"] <= end_date:
                print(row)
        for row in radar:
            if radar["OFFENCE_MONTH"] >= start_date and radar["OFFENCE_MONTH"] <= end_date:
                print(row)


#def showPopularListings(startperiod, endperiod, suburbName='sydney'):

#def insight():

#def showCleanComments():
