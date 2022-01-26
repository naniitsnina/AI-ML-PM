'''Viewing the Data'''
# Ex.1 - Get a quick overview by printing the first 10 rows of the DataFrame using the head() method:
import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))

# Ex.2 - Print the first 5 rows of the DataFrame:
print(df.head())

# Ex.3 - Print the last 5 rows of the DataFrame using the tail() method:
print(df.tail())

'''Info About the Data'''
# Ex.1 - Print information about the data using the info() method:
print(df.info())

'''Result Explained'''
# The result tells us there are 169 rows and 4 columns:
    # RangeIndex: 169 entries, 0 to 168
    # Data columns (total 4 columns):

# And the name of each column with the data type:
    # #   Column    Non-Null Count  Dtype
    # ---  ------    --------------  -----
    #  0   Duration  169 non-null    int64
    #  1   Pulse     169 non-null    int64
    #  2   Maxpulse  169 non-null    int64
    #  3   Calories  164 non-null    float64

'''Null Values'''
# The info() method also tell us how many Non-Null values there are present in each column, and in our data set it seems
# like there are 164 of 169 Non-Null values in the "Calories" column

# Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.

# Empty values, or Null values, can be abd when analyzing data to 'clean data'.