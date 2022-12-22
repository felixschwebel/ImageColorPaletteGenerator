import numpy as np
from PIL import Image
import pandas as pd

test_file = 'static/img/steve-johnson-placeholder.jpg'
test_file2 = 'static/uploads/coffee.jpg'


def convert_to_hex(rbg):
    return '#{:02x}{:02x}{:02x}'.format(rbg[0], rbg[1], rbg[2])


def check_colors(file):
    img = np.array(Image.open(file))
    shape = img.shape
    # flatten the image
    shape_new = img.reshape(shape[0]*shape[1], shape[2])
    hex_df = pd.DataFrame([convert_to_hex(rgb) for rgb in shape_new]).value_counts()[:10]

    hex_colors = [color[0] for color in hex_df.index]
    colors = []
    start = 0
    end = 2
    for i in range(5):
        colors.append(hex_colors[start:end])
        start += 2
        end += 2

    return colors
