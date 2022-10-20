# a pandas DataFrame is a 2D data structure e.g a 2D array, a table with rows and columns

import pandas as pd
myDataset = {
    'Colors': ['Oranage', "Blue", "Yellow"],
    "Say" : ["Better", "Best", "worse"]
}

myvar = pd.DataFrame(myDataset)
print(myvar)

# To return one or more specified rows we sue the loc attribute i.e

MyDataset = {
    'Colors': ['Oranage', "Blue", "Yellow"],
    "Say" : ["Better", "Best", "worse"]
}

Myvar = pd.DataFrame(myDataset)
print(Myvar.loc[2])

# However, the use of attribute .loc[[0,1 ]] results into a series
myDataset = {
    'Colors': ['Oranage', "Blue", "Yellow"],
    "Say" : ["Better", "Best", "worse"]
}

myvar = pd.DataFrame(myDataset)
print(myvar.loc[[0,1]])



# Named index;
import pandas as pd
myDataset = {
    'Colors': ['Oranage', "Blue", "Yellow" ,'Maroon'],
    "Say" : ["Better", "Best", "worse", 'Good']
}

myvar = pd.DataFrame(myDataset, index= ["A", "B", "c", "D"])
print(myvar)

# Load files into a dataframe 
