import numpy

print("Printing Original array")
smpl = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
print (smpl)


mini = numpy.amin(smpl, 1) 
print("Printing amin Of Axis 1")
print(mini)

maxi = numpy.amax(smpl, 0) 
print("Printing amax Of Axis 0")
print(maxi)
