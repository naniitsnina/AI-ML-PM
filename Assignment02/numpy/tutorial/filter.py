'''Filtering Arrays'''
# Ex.1 - Create an array from the elements on index 0 and 2:
import numpy as np
arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

'''Creating the Filter Array'''
# Ex.1 - Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43, 44])

#Create an empty list
filter_arr = []

#go through each element in arr
for element in arr:
    #if the element is higher than 42, set the value to True, otherwise False:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)



# Ex. 1 - Create a filter that will return only even elements form the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])

#Create an empytlist
filter_arr = []

#go through each element in arr
for element in arr:
    #if the element is completely divisible by 2, set the value to True, otherwise False
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)