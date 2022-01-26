'''Read CSV File'''
#  Ex.1 - Load the CSV into a DataFrame
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())

# Ex.2 - Print the DataFrame without the to_string() method:
print(df)

'''Max Rows'''
# Ex.1 - Check the number of maximum returned rows using pd.options.display.max_rows() method:
print(pd.options.display.max_rows)

# Ex.2 - Increase the maximum number of rows to display the entire DataFrame:
pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df)
