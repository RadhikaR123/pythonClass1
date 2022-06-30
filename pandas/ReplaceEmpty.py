import pandas as pd

df = pd.read_csv('/home/navgurukul/Desktop/pythonClass/pandas/dirtyData.csv')

df.fillna(120, inplace = True)     #it will fill all the empty rows with 120

print(df.to_string())
# if we want to replace only a specified columns , then 

df['calories'].fillna(120, inplace = True)     # it will replace empty for only calories column

print(df.to_string())

# ____________________________________________________________

#  Replace using mean()

x= df["calories"].mean()   # it will give the mean of calorie column

df["calories"].fillna(x, inplace = True)



y= df["calories"].median() # it will return median


z= x= df["calories"].mode()[0] # it will return mode
print()

