#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 15:54:45 2021

@author: lachlanwhite
"""

#lachlans second function test - additional function


#list cases determined by specific parameters listed in the analysis tool
#including camera type, location ect.

#Test scenarios for functional requirements - pending for jack to add to GUI

import pandas as pd
from datetime import date

#import data
data = pd.read_csv('penalty_data_set_2.csv', low_memory=False)

#inputs into gui - jack fix
#startdate = search_startperiod #assign variable to button
#enddate = search_endperiod#assign variable to buttom


#print to console all cases based on camera or radar
camera = (data[data.stack().str.contains("Fixed Digital Speed Camera").any(level=0)])
radar = (data[data.stack().str.contains("Radar").any(level=0)])
mcamera = ((data[data.stack().str.contains("Mobile Digital Speed Camera").any(level=0)]))
rcamera = (data[data.stack().str.contains("Red Light / Speed Camera").any(level=0)])

for row in camera:
    if camera["OFFENCE_MONTH"] >= start_date and camera["OFFENCE_MONTH"] <= end_date:
        print(row)

for row in radar:
    if radar["OFFENCE_MONTH"] >= start_date and radar["OFFENCE_MONTH"] <= end_date:
        print(row)

for row in mcamera:
    if mcamera["OFFENCE_MONTH"] >= start_date and mcamera["OFFENCE_MONTH"] <= end_date:
        print(row)

for row in rcamera:
    if rcamera["OFFENCE_MONTH"] >= start_date and rcamera["OFFENCE_MONTH"] <= end_date:
        print(row)



