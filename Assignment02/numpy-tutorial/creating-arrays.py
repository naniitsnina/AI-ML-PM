# Learning by Exercises
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))
arr = np.array([1, 2, 3, 4, 5])

# Learning by Examples
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

# 0-D Arrays
import numpy as np

arr = np.array(42)

print(arr)

# 1-D Arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

# 2-D Arrays
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

# 3-D Arrays
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3,], [4, 5, 6]])

print(arr)

# Check Number of Dimensions?
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3,], [4, 5, 6]])

print(arr)

# Higher Dimensional Arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)