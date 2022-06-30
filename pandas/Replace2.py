import pandas as pd

df = pd.read_csv('/home/navgurukul/Desktop/pythonClass/pandas/dirtyData.csv')

df.loc[7,'Duration'] = 45

print(df.to_string())


# if we want to set 70 in all the values of duration column, then loop through it and put the condition

df = pd.read_csv('/home/navgurukul/Desktop/pythonClass/pandas/dirtyData.csv')

for x in df.index:
    if df.loc[x, "Duration"] >120:
        df.loc[x,"Duration"] = 70
print(df.to_string())




# we can also drop th unwanted row by looping by using drop() method

for i in df.index:
    if df.loc[i,"Duration"] >120:
        df.drop(i, inplace = True)