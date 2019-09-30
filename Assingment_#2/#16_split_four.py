import numpy

print("Creating 8X3 array using numpy.arange")
smpl = numpy.arange(10, 34, 1)
smpl = smpl.reshape(8,3)
print (smpl)

print("\nDividing 8X3 array into 4 sub array\n")
sub = numpy.split(smpl, 4) 
print(sub)
