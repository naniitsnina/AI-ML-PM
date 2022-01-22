'''Iterating Arrays'''
# Ex.1 - Iterate on the elements of the following 1-D array:
import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
    print(x)

'''Iterating 2-D Arrays'''
# Ex.1 - Iterate on the elements of the following 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)

# Ex.2 - Iterate on each scalar element of the 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    for y in x:
        print(y)

'''Iterating 3-D Arrays'''
# Ex.1 - Iterate on the elements of the following 3-D array:
arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]])

for x in arr:
    print(x)

# Ex.2 - Iterate down to the scalars

for x in arr:
    for y in x:
        for z in y:
            print(z)

'''Iterating Arrays Using nditer'''
# Ex.1 - Iterating on each Element
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)

'''Iterating with Different Step Size'''
# Ex.1 - Iterate through every scalar element of the 2D array skipping 1 element
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
    print(x)

'''Enumerate Iteration Using ndenumerate'''
# Enumerate on following 1D arrays elements:
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
    print(idx, x)

# Ex.2 - Enumerate on follwoing 2D array's elements:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
    print(idx, x)