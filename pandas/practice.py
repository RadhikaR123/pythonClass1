from textwrap import indent
import pandas as pd
import json
import matplotlib.pyplot as plt


# df = pd.read_csv('/home/navgurukul/Desktop/pythonClass/pandas/data.csv')
# pf = pd.DataFrame(df)

# print(pf.loc[[0,1,2,3]])

dic= {"name": [1,1,3,4], "work": [5,5,7,8], "city": ["k","k","g","o"]}

with open("practice.json", "w") as f:
    json.dump(dic, f, indent=2)

df = pd.read_json('/home/navgurukul/Desktop/pythonClass/practice.json')

# # pf = pd.DataFrame(dic, index= ["day1","day2","day3","day4"] )
# print(df.duplicated())
# new_df= df.drop_duplicates()

# print(new_df)



# df.loc[0,"name"]= "radhi"

# for i in df.index:
#     if df.loc[i,"city"] == "k":
#         df.loc[i,"city"] = "R"

# print(df)

print(df.corr())



#plotting of data

# df.plot(kind = 'scatter', x= 'name', y='work')

df["name"].plot(kind = 'hist')
plt.show()