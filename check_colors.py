import numpy as np
from PIL import Image

test_file = 'static/img/steve-johnson-placeholder.jpg'


def convert_to_hex(rbg):
    return '#{:02x}{:02x}{:02x}'.format(rbg[0], rbg[1], rbg[2])


def check_colors(file):
    img = np.array(Image.open(file))
    # flatten the image
    shape_new = img.reshape(2483*3493, 3)
    # use numpy histogram to sort the colors into 10 buckets
    indices = np.histogram(shape_new, bins=10)[0]
    # get rbg colors from array
    rgb_colors = [shape_new[color] for color in indices]
    # convert to hex
    hex_colors = [convert_to_hex(value) for value in rgb_colors]
    return hex_colors


check_colors(test_file)