import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('penalty_data_set_2.csv', low_memory=False)

#Analysing the cases caused by mobile phone usage - ie: trend over time, offence code, and so on. Jack

#get all mobile phone cases
results = (data[data.stack().str.contains("mobile phone").any(level=0)])


    








