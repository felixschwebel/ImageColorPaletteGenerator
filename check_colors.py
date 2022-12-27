import numpy as np
from PIL import Image


# test_file = 'static/img/steve-johnson-placeholder.jpg'


def convert_to_hex(rbg):
    return '#{:02x}{:02x}{:02x}'.format(rbg[0], rbg[1], rbg[2])


def check_colors(file):
    # open image as numpy array
    img = np.array(Image.open(file))
    shape = img.shape
    # flatten the image
    shape_new = img.reshape(shape[0]*shape[1], shape[2])
    # use numpy histogram to sort the colors into 10 buckets
    indices = np.histogram(shape_new, bins=10)[0]
    # get rbg colors from array
    try:
        rgb_colors = [shape_new[color] for color in indices]
    except IndexError:
        return False
    # convert to hex
    hex_colors = [convert_to_hex(value) for value in rgb_colors]

    # change the list format
    colors = []
    start = 0
    end = 2
    for i in range(5):
        colors.append(hex_colors[start:end])
        start += 2
        end += 2

    return colors

