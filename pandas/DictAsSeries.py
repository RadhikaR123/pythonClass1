# creating a simple pandas series from a dictionary

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)


# creating series using data only day1 and day2

myvar1 = pd.series(calories, index = ["day1", "day2"])
print(myvar1)