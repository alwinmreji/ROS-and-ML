import numpy as np

print("Creating 5X2 array using np.arange")
smpl = np.arange(100, 200, 10)
smpl = smpl.reshape(5,2)
print (smpl)
# OUTPUT
# Creating 5X2 array using np.arange
# [[100 110]
#  [120 130]
#  [140 150]
#  [160 170]
#  [180 190]]
