import pandas as pd


df = pd.read_csv('/home/navgurukul/Desktop/pythonClass/pandas/dirtyData.csv')

print(df.duplicated())

# to drop the duplicates , we use....

x=df.drop_duplicates()
print(x.to_string())
