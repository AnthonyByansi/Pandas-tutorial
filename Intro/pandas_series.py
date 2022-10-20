# Pandas series is like a sa column is a table. It is basiscally a 1D array holding data of any type.

import pandas as pd 

colors = ['Orange', 'blue', "red"]
myVar = pd.Series(colors)

print(myVar[1]) # this shall return the element at index 1


"""
mydataset = {
    "colours" : ['Blue', 'orange', "Yellow"],
    "Saying" : ["Most favourite", "Better", "worst of all"]
}

myVarz = pd.DataFrame(mydataset)
print(myVarz)

"""


# creating Labels. Labels enable us to access an item by referring to the label.



companies = ["apple", "Google", "Amazon" ,"Microsoft"]
campz = pd.Series(companies, index = ["x", "y", "z", 'D'])
print(campz['D'])


# Key/value Objects as series 

colors = {"color1": "Blue", "color2": "Red", "color3":"Orange" }
    
myColors = pd.Series(colors)
print(myColors)


# DataFrames " dataframes are pandas datasets that are usually multi-dimensional tables"
# Series is like a column and a DataFrame is the whole table.

import pandas as pd 
mydataset = {
    "colours" : ['Blue', 'orange', "Yellow"],
    "Say" : ["Most favourite", "Better", "worst of all"]
}

myVar = pd.DataFrame(mydataset)
print(myVar)