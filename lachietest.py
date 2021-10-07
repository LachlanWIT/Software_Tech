#Test scenarios for functionaln requirements - pending for jack to add to GUI

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

#import data
data = pd.read_csv('penalty_data_set_2.csv', low_memory=False)

#For a user-selected period, 
#retrieve all cases captured by radar or camera based on offence 


#assign variable name for if statement from global button variable in GUI
startdate = search_startperiod
enddate = search_endperiod 


#print to console all cases based on camera or radar

camera = (data[data.stack().str.contains("Camera Detected").any(level=0)])
radar = (data[data.stack().str.contains("Radar").any(level=0)])

#apply date range filter

for row in camera:
    if camera["OFFENCE_MONTH"] >= startdate and camera["OFFENCE_MONTH"]<= enddate:
        print(row)
        
        
