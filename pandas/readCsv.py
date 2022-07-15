import pandas as pd

df = pd.read_csv('/home/navgurukul/Desktop/pythonClass/pandas/data.csv')
# print(df)    #it will return first and last 5 rows

# print(df.to_string())     # it will return whole file

print(pd.options.display.max_rows)       #it will return the maximum number of rows.
