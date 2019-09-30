import numpy

arr1 = numpy.array([[5, 6, 9], [21 ,18, 27]])
arr2 = numpy.array([[15 ,33, 24], [4 ,7, 1]])

result  = arr1 + arr2
print("addition of two arrays is \n")
print(result)

for num in numpy.nditer(result, op_flags = ['readwrite']):
   num[...] = num*num
print("\nResult array after calculating the square root of all elements\n")
print(result)

# OUTPUT
# addition of two arrays is

# [[20 39 33]
#  [25 25 28]]

# Result array after calculating the square root of all elements

# [[ 400 1521 1089]
#  [ 625  625  784]]
