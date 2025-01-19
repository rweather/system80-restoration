#!/usr/bin/python3
#
# Dump the System 80 character generator ROM to a PNG.
#
# Input:  Z25-52116-Character-Generator.bin
# Output: character-set.png

import io
import sys
from PIL import Image

with open('Z25-52116-Character-Generator.bin', 'rb') as file:
    file_data = file.read()

image = Image.new('RGB', (8 * 16 * 2, 16 * 12 * 2))
for ch in range(256):
    for y in range(12):
        bits = file_data[ch * 16 + y]
        for x in range(8):
            if (bits & (0x80 >> x)) != 0:
                px = ((ch % 16) * 8 + x) * 2
                py = ((int((ch & 0xF0) / 16) * 12) + y) * 2
                image.putpixel((px, py), (0, 255, 0))
                image.putpixel((px + 1, py), (0, 255, 0))
                image.putpixel((px, py + 1), (0, 255, 0))
                image.putpixel((px + 1, py + 1), (0, 255, 0))
                image.putpixel((px, py), (0, 255, 0))

image.save('character-set.png')
