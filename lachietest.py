#Test scenarios for functionaln requirements - pending for jack to add to GUI

import csv

with open('penalty_data_set_2.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)