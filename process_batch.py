#! /usr/bin/python

import os
from pathlib import Path


INPUT_DIR = Path('./batch/')
OUTPUT_DIR = Path('./output/')
CMD_TEMPLATE = 'python main.py --image "{}" --output "{}" --watermark_type sb --scale 0.9'


files = os.listdir(INPUT_DIR)
for (index, filename) in enumerate(files):
    input_path = INPUT_DIR / filename
    output_path = OUTPUT_DIR / filename
    os.system(CMD_TEMPLATE.format(input_path, output_path))

    print("##################################################")
    print(f"Processed image {index} of {len(files)}")
    print("##################################################")

print("Completed")
