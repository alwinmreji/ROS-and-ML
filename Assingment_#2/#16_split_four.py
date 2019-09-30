import numpy

print("Creating 8X3 array using numpy.arange")
smpl = numpy.arange(10, 34, 1)
smpl = smpl.reshape(8,3)
print (smpl)

print("\nDividing 8X3 array into 4 sub array\n")
sub = numpy.split(smpl, 4) 
print(sub)

# OUTPUT
# Creating 8X3 array using numpy.arange
# [[10 11 12]
#  [13 14 15]
#  [16 17 18]
#  [19 20 21]
#  [22 23 24]
#  [25 26 27]
#  [28 29 30]
#  [31 32 33]]

# Dividing 8X3 array into 4 sub array

# [array([[10, 11, 12],
#        [13, 14, 15]]), array([[16, 17, 18],
#        [19, 20, 21]]), array([[22, 23, 24],
#        [25, 26, 27]]), array([[28, 29, 30],
#        [31, 32, 33]])]
