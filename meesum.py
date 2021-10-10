#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:43:32 2021

@author: lachlanwhite
"""
# Meesum requirement !

# importing the module
import pandas as pd

data = pd.read_csv('penalty_data_set_2.csv', low_memory=False)


def searchByDate(start_date, end_date):
    for row in data:
        if data['OFFENCE_MONTH'] >= start_date and data["OFFENCE_MONTH"] <= end_date:
            print(row)
