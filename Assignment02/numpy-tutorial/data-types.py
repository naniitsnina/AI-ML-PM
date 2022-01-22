'''Data Types in Python'''
# strings - used to represent text data, the text is given under quote marks. e.g."ABCD"
# integer - used to represent integer numbers. e.g. -1, -2, -3
# float - used to represent real numbers. e.g. 1.2, 42.42
# boolean -  used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

'''Data Types in NumPy'''
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - String
# U - unicode string
# V - fixed chunk of memory for other type(void)

'''Checking the Data Type of an Array'''
# Get the data type of an array object:
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

# get the data type of an array containing strings:
arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

'''Creating Arrays With a Defined Data Type'''
# Ex.1 - Create an array with data type string:
arr = np.array([1, 2, 3, 4,], dtype ='S')

print(arr)
print(arr.dtype)

# Ex.2 - Create an array with data type 4 butes integer:
arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

'''Converting Data Type on Existing Arrays'''
# Change data type from float to integer by using 'i' as parameter value:
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

# Change data type from float to integer by using int as parameter value:
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

# Change data type from intger to boolean:

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)