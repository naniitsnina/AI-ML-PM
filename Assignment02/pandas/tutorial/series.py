'''What is a Series'''
# Ex.1 - Create a simply Pandas Series from a list:
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

'''Labels'''
# Return the first value of the Series:
print(myvar[0])

'''Create Labels'''
# Ex.1 - Create your own labels:
myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

# Ex.2 - Return to the value of "y":
print(myvar["y"])

'''Key/Value Objects as Series'''
# Ex.1 - Create a simple Pandas Series from a dictionary:
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

# Ex.2 - Create a Series using only data from "day1" and "day2":
myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

'''Data Frames'''
# Ex.1 - Create a Data Frame from two Series:
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)