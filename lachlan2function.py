#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 15:54:45 2021

@author: lachlanwhite
"""

#lachlans second function test - additional function


#list all cases alyse the number of cases determined by specific parameters listed in the analysis tool
#including camera type, location ect.

#Test scenarios for functionaln requirements - pending for jack to add to GUI

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

#import data
data = pd.read_csv('penalty_data_set_2.csv', low_memory=False)

#inputs into gui - jack fix
startdate = search_startperiod #assign variable to button
enddate = search_endperiod#assign variable to buttom


#print to console all cases based on camera or radar

camera = (data[data.stack().str.contains("Camera Detected").any(level=0)])
radar = (data[data.stack().str.contains("Radar").any(level=0)])
driver = (data[data.stack().str.contains("Police").any(level=0)])
rcamera = (data[data.stack().str.contains("Red Light Camera").any(level=0)])




for row in camera:
    if row 



