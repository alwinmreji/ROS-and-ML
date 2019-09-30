import numpy

smpl = numpy.array([[10 ,12, 13], [14, 15, 16], [7, 8, 9]]) 
print("Printing Input Array")
print(smpl)

print("\n Printing array of items in the third column from all rows")
nwarr = smpl[...,1]
print(nwarr)

# OUTPUT
# Printing Input Array
# [[10 12 13]
#  [14 15 16]
#  [7 8 9]]
#  Printing array of items in the third column from all rows
# [12 15 8]
