#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:43:32 2021

@author: lachlanwhite
"""
#Meesum requirement !

# importing the module
import csv

def searchByDate():
    year = str(input('Enter year to show data: '))
    csv_file=csv.reader(open('penalty_data_set_2.csv', 'r'))

    for row in csv_file:
        if year in row[0]:
            print(row)

print('Enter 0 to search for year')

src = int(input('Input: '))

if src==0:
    searchByDate()
else:
    print('sorry invalid year')
