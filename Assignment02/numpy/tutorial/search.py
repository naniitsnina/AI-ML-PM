'''Searching Arrays'''
# Ex.1 - Find the indexes where the value is 4 use the where() method:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr==4)

print(x)

# Ex.2 - Find the indexes where the values are even:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)

# Ex.3 - Find the indexes where the values are odd:
x = np.where(arr%2 == 1)

print(x)

'''Sorted'''
# Ex.1 - Find the indexes where the value 7 should be inserted, use the searchsorted() method:
arr = ([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)

'''Search from the Right Side'''
# Ex.1 - Find the indexes where the value 7 should be inserted, starting from the right:
x = np.searchsorted(arr, 7, side='right')

print(x)

'''Multiple Values'''
# Ex.1 - Find the indexes where the values 2, 4, and 6 should be inserted:
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)