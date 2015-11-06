#!/usr/bin/env python

"""
Inspired by https://github.com/JuanPotato/Legofy
This program uses post it notes instead of legos
"""

try:
    from PIL import Image
except ImportError:
    exit("Install Pillow, pip install Pillow")

import argparse
import os

POST_IT_SIZE = 76 # mm
POST_IT_IMAGE_SIZE = POST_IT_SIZE / 2
USE_POST_IT_COLORS = True

# Base colors http://www.post-it.com/3M/en_US/post-it/ideas/color
# Picked using color picker so colors may not be exact

POST_IT_COLORS = (

    # Also include black and white colors
    '#000000',
    '#FFFFFF',

    # Rio de Janeiro theme
    '#FBAE3C',
    '#FD4DB0',
    '#1DACE6',
    '#E7F150',
    '#FFD938',

    # Marrakesh
    '#EE5F35',
    '#F8BD49',
    '#E7DF34',
    '#86A6D5',
    '#A2509A',

    # Bora Bora
    '#E7DF34',
    '#35A8A1',
    '#BFDDD3',
    '#DAE3EA',
    '#18ADE8',

    # Bali
    '#A9C6E8',
    '#6185C1',
    '#F4A89B',
    '#D47698',
    '#B4AACD',

    # New york
    '#FFD938',
    '#90909A',
    '#D6D4DF',
    '#B3CCE2',
    '#1DACE6',

    # Jaipur
    '#1DACE6',
    '#35A8A1',
    '#EE5F35',
    '#F37D93',
    '#FFD938',

    # Capetown
    '#FF6C88',
    '#FBAE3C',
    '#3BD7C1',
    '#FD4DB0',
    '#E7F152',

    # Marseille
    '#D6769B',
    '#FBF7AE',
    '#BFDDD3',
    '#F3AEC1',
    '#D2617F',

    # Helsinki
    '#303030',
    '#FBF7AE',
    '#DAE3EA',
    '#96969B',
    '#D6D4DF',
)

def init_from_hex(hexcodes):
    codes = [v.strip('#') for v in hexcodes]
    def rgb(color):
        return [int(a, 16) for a in (color[0:2], color[2:4], color[4:6])]
    return tuple([rgb(code) for code in codes])

_POST_IT_COLOR_TUPLES = init_from_hex(POST_IT_COLORS)

def postit(color):
    def black_or_white(i):
        if i % 2 == 0:
            return (0, 0, 0)
        else:
            return (255, 255, 255)

    r, g, b = color
    color = "rgb(%s, %s, %s)" % (r, g, b)
    im = Image.new("RGB", (POST_IT_IMAGE_SIZE, POST_IT_IMAGE_SIZE), color)
    pix = im.load()
    for i in range(POST_IT_IMAGE_SIZE):
        col = black_or_white(i)
        pix[0, i] = col
        pix[i, 0] = col
        pix[POST_IT_IMAGE_SIZE - 1, i] = col
        pix[i, POST_IT_IMAGE_SIZE - 1] = col
    return im


def color_distance(first, second):
    # http://www.compuphase.com/cmetric.htm
    rmean = (first[0] + second[0]) / 2
    r, g, b = [a - b for a,b in zip(first, second)]
    # ommited sqrt
    return (((512+rmean)*r*r)>>8) + 4*g*g + (((767-rmean)*b*b)>>8)

def nearest_color(color):
    if USE_POST_IT_COLORS:
        return min(_POST_IT_COLOR_TUPLES, key=lambda x : color_distance(color, x))
    return color


def make_postit(image):
    w, h = image.size
    pw, ph = w * POST_IT_IMAGE_SIZE, h * POST_IT_IMAGE_SIZE
    newimage = Image.new("RGB", (pw, ph))
    pixels = image.load()
    for x in range(w):
        for y in range(h):
            px = x * POST_IT_IMAGE_SIZE
            py = y * POST_IT_IMAGE_SIZE
            color = nearest_color(pixels[x, y])
            pim = postit(color)
            newimage.paste(pim, (px, py))
    return newimage

def image_to_postit(fname, wallsize):
    """
    fname - file name of image
    wallsize - (w, h) in millimeters
    """
    w, h = wallsize # in mm
    # Number of post-its that can be fit in wall
    nposts= min(w / POST_IT_SIZE, h / POST_IT_SIZE)
    fname = os.path.realpath(os.path.expanduser(fname))
    with open(fname) as f:
        im = Image.open(f)
        imw, imh = im.size
        # Shrink image such that each pixel becomes a post it
        shrink = min(imw / nposts, imh / nposts)
        im.thumbnail((imw / shrink, imh / shrink))
        if im.mode == "RGBA":
            # Replace transparent areas with white
            background = Image.new("RGB", im.size, (255, 255, 255))
            background.paste(im, mask=im.split()[3])
            im = background
        post_im = make_postit(im)
        post_im.show()

def main():
    parser = argparse.ArgumentParser(
        description="Convert an image to decoratable post it notes")
    parser.add_argument("-i", "--image", help="Input image file", required=True)
    parser.add_argument(
        "-W", "--width", help="Width of wall in mm", type=int, default=2000)
    parser.add_argument(
        "-H", "--height", help="Height of wall in mm", type=int, default=2000)
    parser.add_argument(
        "--only-postit-colors", help="Uses only colors from post it notes",
        action="store_true")

    global USE_POST_IT_COLORS
    args = parser.parse_args()
    print args
    USE_POST_IT_COLORS = args.only_postit_colors

    image_to_postit(args.image, (args.width, args.height))

if __name__ == '__main__':
    main()
