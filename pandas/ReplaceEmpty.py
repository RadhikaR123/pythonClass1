import pandas as pd

df = pd.read_csv('/home/navgurukul/Desktop/pythonClass/pandas/dirtyData.csv')

df.fillna(120, inplace = True)     #it will fill all the empty rows with 120

# if we want to replace only a specified columns , then 

df['calories'].fillna(120, inplace = True)     # it will replace empty for only calories column
