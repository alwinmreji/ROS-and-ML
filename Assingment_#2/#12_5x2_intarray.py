import numpy as np

print("Creating 5X2 array using np.arange")
smpl = np.arange(100, 200, 10)
smpl = smpl.reshape(5,2)
print (smpl)
