#Test scenarios for functionaln requirements - pending for jack to add to GUI

import pandas as pd
from datetime import date

#import data
data = pd.read_csv('penalty_data_set_2.csv', low_memory=False)
#For a user-selected period, 
#retrieve all cases captured by radar or camera based on offence 


#assign variable name for if statement from global button variable in GUI
start_date = date(2014, 1, 1)
end_date = date(2016, 1, 1)

#function
def function_1(start_date, end_date):
    camera = (data[data.stack().str.contains("Camera Detected").any(level=0)])
    radar = (data[data.stack().str.contains("Radar").any(level=0)])
    for row in camera:
        if camera["OFFENCE_MONTH"] >= start_date and camera["OFFENCE_MONTH"] <= end_date:
            print(row)
    for row in radar:
            if radar["OFFENCE_MONTH"] >= start_date and radar["OFFENCE_MONTH"] <= end_date:
             print(row)

        
