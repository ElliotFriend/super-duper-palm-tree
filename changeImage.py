#!/usr/bin/env python3

import os

from PIL import Image

# In this section, you will write a Python script named changeImage.py
# to process the supplier images. You will be using the PIL library to
# update all images within ~/supplier-data/images directory to the
# following specifications:
#
# - Size: Change image resolution from 3000x2000 to 600x400 pixel
# - Format: Change image format from .TIFF to .JPEG

dir = 'supplier-data/images/'
all_images = os.listdir(dir)

for image in all_images:
    f, e = os.path.splitext(image)
    outfile = dir + f + '.jpeg'
    try:
        with Image.open(image) as im:
            im = im.resize((600, 400))
            im = im.convert("RGB")
            im.save(outfile)
    except OSError:
        print("cannot convert", image)
