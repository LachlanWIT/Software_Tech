
import pandas as pd

data = pd.read_csv('penalty_data_set_2.csv', low_memory=False)

def function2_digital(start_date, end_date):
 camera = (data[data.stack().str.contains("Fixed Digital Speed Camera").any(level=0)])
 for row in camera:
    if camera["OFFENCE_MONTH"] >= start_date and camera["OFFENCE_MONTH"] <= end_date:
        print(row)


def function2_radar(start_date, end_date):
 radar = (data[data.stack().str.contains("Radar").any(level=0)])
 for row in radar:
    if radar["OFFENCE_MONTH"] >= start_date and radar["OFFENCE_MONTH"] <= end_date:
        print(row)


def function2_mobile(start_date, end_date):
 mcamera = ((data[data.stack().str.contains("Mobile Digital Speed Camera").any(level=0)]))
 for row in mcamera:
    if mcamera["OFFENCE_MONTH"] >= start_date and mcamera["OFFENCE_MONTH"] <= end_date:
        print(row)


def function2_red(start_date, end_date):
 rcamera = (data[data.stack().str.contains("Red Light / Speed Camera").any(level=0)])
 for row in rcamera:
    if rcamera["OFFENCE_MONTH"] >= start_date and rcamera["OFFENCE_MONTH"] <= end_date:
        print(row)




