'''Splitting NumPy Arrays'''
# Ex.1 - Split array in 3 parts using array_split():
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6 ])

newarr = np.array_split(arr, 3)

print(newarr)

# Ex.2 - Split the array in 4 parts:
newarr = np.array_split(arr, 4)

print(newarr)

'''Split Into Arrays'''
# Ex.1 - Access the splitted arrays:
newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

'''Splitting 2-D Arrays'''
# Ex.1 - Split the 2-D array into three 2-D arrays.
arr = np.array([[1, 2], [3,4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

# Ex.2 - Split the 2-D array into three 2-D arrays.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)

# Ex.3 - Split the 2-D array into three 2-D arrays along rows.
newarr = np.array_split(arr, 3, axis=1)

print(newarr)

# Ex.4 - Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.

newarr = np.hsplit(arr, 3)

print(newarr) 