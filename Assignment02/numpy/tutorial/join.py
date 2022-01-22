'''Joining NumPy Arrays'''
# Ex.1 - Join two arrays
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

# Ex.2 - Join two 2D arrays along rows (axis=1):
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

'''Joining Arrays Using Stack Functions'''
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

'''Stacking Along Rows'''
# Ex. 1 - NumPy provides a helper function: hstack() to stack along rows.
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)

'''Stacking Along Comumns'''
# Ex. 1 - NumPy provides a helper function: vstack()  to stack along columns.
arr = np.vstack((arr1, arr2))

print(arr)

'''Stacking Along Height(depth)'''
# Ex.1 - NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
arr = np.dstack((arr1, arr2))

print(arr)

