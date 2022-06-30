# create a simple Pandas Dataframe.......

import pandas as pd

data = {
    "a" : [1,2,3,4],
    "b" : [5,6,7,8]
}

df = pd.DataFrame(data)

print(df)

#  if we want to return one or more specified rows....

print(df.loc[0])
print(df.loc[[0,1]])


# if we want to cahnge the index name then.........

df1 = pd.DataFrame(data, index = ["day1","day2","day3","day4"])

print(df1)

# to return specified "row, use "loc"

print(df1.loc["day2"])