#!/usr/bin/env python3

import os
import requests

# Now, you'll have to process the .txt files (named 001.txt, 002.txt,
# ...) in the supplier-data/descriptions/ directory and save them in a
# data structure so that you can then upload them via JSON.

im_dir = "supplier-data/images/"
desc_dir = "supplier-data/descriptions/"
url = "http://[linux-instance-external-IP]/fruits/"

desc_files = os.listdir(dir)
for file in desc_files:
    supplier_data = {}
    with open(desc_dir + file) as f:
        supplier_data['name'] = f.readline().rstrip('\n')
        supplier_data['weight'] = f.readline().rstrip('\n')
        supplier_data['description'] = f.readline().rstrip('\n')
        #supplier_data['image_name'] =

        response = requests.post(url, json=supplier_data)
        response.raise_for_status()
