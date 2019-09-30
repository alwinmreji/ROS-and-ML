import numpy

nwarr = numpy.array([[1 ,2, 3, 4], [5 ,6, 7, 8], 
[9 ,10, 11, 12], [13 ,14, 15, 16], [17 ,18, 19, 20]]) 
print("Printing Input Array")
print(nwarr)

print("\n Printing array of odd rows and even columns")
newArray = nwarr[::2, 1::2]
print(newArray)

# OUTPUT
# Printing Input Array
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]
#  [17 18 19 20]]

#  Printing array of odd rows and even columns
# [[ 2  4]
#  [10 12]
#  [18 20]]
