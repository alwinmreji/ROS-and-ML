import numpy

print("Printing Original array")
smpl = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
print (smpl)

print("Array after deleting column 2 on axis 1")
smpl = numpy.delete(smpl , 1, axis = 1) 
print (smpl)

arr = numpy.array([[10,10,10]])

print("Array after inserting column 2 on axis 1")
smpl = numpy.insert(smpl , 1, arr, axis = 1) 
print (smpl)

# OUTPUT
# Printing Original array
# [[34 43 73]
#  [82 22 12]
#  [53 94 66]]
# Array after deleting column 2 on axis 1
# [[34 73]
#  [82 12]
#  [53 66]]
# Array after inserting column 2 on axis 1
# [[34 10 73]
#  [82 10 12]
#  [53 10 66]]
