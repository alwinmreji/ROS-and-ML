import numpy as np

first = np.empty([4,2], dtype = np.uint16) 
print("Printing Array")
print(first)

print("Printing np array Attributes")
print("1> Array Shape is: ", first.shape)
print("2>. Array dimensions are ", first.ndim)
print("3>. Length of each element of array in bytes is ", first.itemsize)
