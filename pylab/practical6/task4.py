import numpy as np
import os
from skimage import io
import matplotlib.pyplot as plt
#Image Operations
img = os.path.join("download.jpeg")
temp = io.imread(img)
io.imshow(temp)
io.show()
temp1 = io.imread(img, as_gray=True)
io.imshow(temp1)
io.show()
print(np.shape(temp1))
cropped_image = temp1[0:100,0:100]
plt.imshow(cropped_image)
plt.show()

