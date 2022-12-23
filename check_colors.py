import numpy as np
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

test_file = 'static/img/steve-johnson-placeholder.jpg'
test_file2 = 'static/uploads/coffee.jpg'


def convert_to_hex(rbg):
    return '#{:02x}{:02x}{:02x}'.format(rbg[0], rbg[1], rbg[2])


def check_colors(file):
    img = np.array(Image.open(file))
    shape = img.shape
    # flatten the image
    shape_new = img.reshape(shape[0]*shape[1], shape[2])
    df = pd.DataFrame()
    hex_series = pd.Series([convert_to_hex(rgb) for rgb in shape_new])
    df['colors'] = hex_series
    df.value_counts()
    #hex_df.hist(column=hex_df, bins=10)
    #plt.show()

    hex_colors = [color[0] for color in hex_df.index]
    colors = []
    start = 0
    end = 2
    for i in range(5):
        colors.append(hex_colors[start:end])
        start += 2
        end += 2

    return colors


check_colors(test_file2)