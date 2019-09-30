import numpy as np

first = np.empty([4,2], dtype = np.uint16) 
print("Printing Array")
print(first)

print("Printing np array Attributes")
print("1> Array Shape is: ", first.shape)
print("2>. Array dimensions are ", first.ndim)
print("3>. Length of each element of array in bytes is ", first.itemsize)
#OUTPUT
# Printing Array
# [[64757 19267]
#  [45868 33230]
#  [16280 54129]
#  [32584     0]]
# Printing numpy array Attributes
# 1> Array Shape is:  (4, 2)
# 2>. Array dimensions are  2
# 3>. Length of each element of array in bytes is  2
