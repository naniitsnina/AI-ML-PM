'''Reshape from 1-D to 2-D'''
# Convert the following 1-D with 12 elements into a 2-D array. The outermost dimension will have 4 arrays, each with 3 elements:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

# Convert the following 1-D array with 12 elements into a 3-D array. The outermost dimension will have 2 arrays that contiains 3 arrays, each with 2 elements
newarr = arr.reshape(2, 3, 2)

print(newarr)

'''Returns Copy or View?'''
# Ex.1 - Check if the returned array is a copy or a view:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)

'''Unknown Dimension'''
# Ex.1 - Covert 1-D array with 8 elements to 3D array with 2x2 elements

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

'''Flattening the arrays'''
# Ex.1 - Convert the array into a 1-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = np.reshape(-1)

print(newarr)
