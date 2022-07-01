import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/navgurukul/Desktop/pythonClass/pandas/data.csv')

df.plot() # it will simply plot the data

df.plot(kind = 'scatter', x='Duration', y="Calories")    # it will plot the data on x and y axis.

df["Duration"].plot(kind = 'hist')       # it will take only one column and show on historical bar
plt.show()