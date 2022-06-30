# Create a simple python series from list....

# import pandas as pd

# a= [1,2,3,4,5]

# pf = pd.Series(a)

# print(pf)


import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)



# if we want to return the first value of the series, 
# we will use label(index)

print(myvar[0])


#  we can also create our own lable, like-

var1= pd.Series(a, index = ['x', 'y','z'])

print(var1)

print(var1["z"])