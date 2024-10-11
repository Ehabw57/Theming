#!/usr/bin/python
import re
from sys import argv

if len(argv) > 2:
    print("usgag**")
    exit(1)


def extract_hex_colors(text):
    hex_color_pattern = r'0x[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{6}'
    hex_colors = re.findall(hex_color_pattern, text)
    return hex_colors[4:]


if __name__ == "__main__":
    with open(argv[1], 'r') as file:
        text = file.read()
    detected_colors = extract_hex_colors(text)
    for i, color in enumerate(detected_colors, 0):
        detected_colors[i] = color.replace('0x', '#')
    print('\n'.join(detected_colors))
