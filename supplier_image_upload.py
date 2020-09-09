#!/usr/bin/env python3

import glob
import requests

url = "http://localhost/upload/"
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})

# You are going to write a script named supplier_image_upload.py that
# takes the jpeg images from the supplier-data/images directory that
# you've processed previously and uploads them to the web server fruit
# catalog.

# [linux-instance-IP-Address]/upload

im_dir = "supplier-data/images/"
url = "http://[linux-instance-IP-Address]/upload/"

jpeg_images = glob.glob(im_dir + '*.jpeg')
for im in jpeg_images:
    with open(im, 'rb') as opened_im:
        response = requests.post(url, files={'file': opened_im})
        response.raise_for_status()
