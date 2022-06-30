import pandas as pd

df = pd.read_csv('/home/navgurukul/Desktop/pythonClass/pandas/dirtyData.csv')

new_df = df.dropna()       # it will remove empty rows, but it will not change the original file

print(new_df.to_string())


# if we want to permanently change the original file..
# use " inplace = True" method

df.dropna(inplace= True)

print(df. to_string())
