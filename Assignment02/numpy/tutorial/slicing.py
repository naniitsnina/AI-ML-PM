'''Slicing Arrays'''

# Ex. 1 - slice from index 1 to index 5
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

# Ex. 2 - slice from index 4 to the end of the array
print(arr[4:])

'''Negative Slicing'''
print(arr[-3:-1])

'''Step'''
# Ex.1 - Return every other element from index 1 to index 5:
print(arr[1:5:2])

# Ex.2 - Return every other element from the array:
print(arr[::2])

'''Slicing 2-D Arrays'''
# Ex.1 - From the second element, since elements from index 1 to index 4(not included):
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

# Ex.2 - From both elements, return index 2:
print(arr[0:2, 2])

# Ex.3 - From both elements, slice index 1 to index 4(not included), this will return a 2-D array:
print(arr[0:2, 1:4])

