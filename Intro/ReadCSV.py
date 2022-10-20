"""We can store big datasets by using CSV files"""
import pandas as pd 
df = pd.read_csv('microsoft_stocks.csv')
df.head()

print(df.head().to_string) # Prints the entire DataFrame
print(df.head())

df.tail()
df.head()

# Maximum rows 
print(pd.options.displaly.max_rows)
