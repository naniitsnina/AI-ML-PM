'''What is a DataFrame?'''
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# load data into a DataFrame ojbect:
df = pd.DataFrame(data)

print(df)

'''Locate Row'''
# Ex.1 - Return row 0, refer to the row index:
print(df.loc[0])

# Ex.2 - Return 0 and 1:
print(df.loc[[0, 1]])

'''Named Indexes'''
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)

'''Located Named Indexes'''
# Ex.1 - Return "day2":
# refer to the named index
print(df.loc["day2"])

'''Load Files Into a DataFrame'''
# Ex.1 - Load a comma separated file (CSV file) into a DataFrame:
df = pd.read_csv('data.csv')

print(df)

