import numpy as np
from PIL import Image
from scipy.stats import mode
import matplotlib.pylot as plt

img = np.array(Image.open('static/img/steve-johnson-placeholder.jpg'))

# print(img.shape)
# output: (2483, 3493, 3)

# print(img[100, 100])
# output: [  5 105 164]

shape_new = img.reshape(2483*3493, 3)
values, counts = np.unique(shape_new, return_counts=True, axis=0)
sort_counts = np.argsort(-counts)

plt.hist(shape_new, bins=100, range=[0, 256])
plt.show()