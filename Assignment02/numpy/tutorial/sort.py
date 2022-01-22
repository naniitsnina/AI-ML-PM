'''Sorting Arrays'''
# Ex.1 - Sort the Array using sort():
import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

# Ex.2 - Sort the array alphabetically:
arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

# Ex.3 - Sort a boolean array:
arr = np.array([True, False, True])

print(np.sort(arr))

'''Sorting a 2-D Array'''
# Ex.1 - Sort a 2-D array:
arr = np.array([[3, 2, 4,], [5, 0, 1]])

print(np.sort(arr))
