#!/usr/bin/python3
import os
from sys import argv

if len(argv) < 2:
    print("usage: fuck you just pass a file")
    exit()

colorscheme = argv[1]


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def is_valid_hex(hex_color):
    return hex_color.startswith('#') and len(hex_color) == 7 \
            and all(c in '0123456789abcdefABCDEF' for c in hex_color[1:])


def read_colors(filename):
    with open(filename, 'r') as file:
        colors = []
        i = 0
        for line in file.readlines():
            color = line.strip()
            i += 1
            if color.startswith(';'):
                continue
            if not is_valid_hex(color):
                print(f"Error at line {i}: [{color}] is invalid hex format.")
                exit(1)

            colors.append(color)
    return colors


def generate_alacritty(colors):
    alacritty_config = f"""
[colors.primary]
background = '{colors[0]}'
foreground = '{colors[7]}'

[colors.normal]
black = '{colors[0]}'
red = '{colors[1]}'
green = '{colors[2]}'
yellow = '{colors[3]}'
blue = '{colors[4]}'
magenta = '{colors[5]}'
cyan = '{colors[6]}'
white = '{colors[7]}'

[colors.bright]
black = '{colors[8]}'
red = '{colors[9]}'
green = '{colors[10]}'
yellow = '{colors[11]}'
blue = '{colors[12]}'
magenta = '{colors[13]}'
cyan = '{colors[14]}'
white = '{colors[15]}'
"""
    return alacritty_config.strip()


def generate_bspwm(colors):
    bspwm_config = f"""
bspc config focused_border_color "{colors[3]}"
bspc config normal_border_color "{colors[8]}"
"""
    return bspwm_config.strip()


def generate_polybar(colors):
    polybar_config = f"""
[colors]
base00 = {colors[0]}
base01 = {colors[1]}
base02 = {colors[2]}
base03 = {colors[3]}
base04 = {colors[4]}
base05 = {colors[5]}
base06 = {colors[6]}
base07 = {colors[7]}
base08 = {colors[8]}
base09 = {colors[9]}
base0A = {colors[10]}
base0B = {colors[11]}
base0C = {colors[12]}
base0D = {colors[13]}
base0E = {colors[14]}
base0F = {colors[15]}
"""
    return polybar_config


def generate_rofi(colors):
    rofi_config = f"""
* {{
    red:                         rgb {hex_to_rgb(colors[1])};
    blue:                        rgb {hex_to_rgb(colors[4])};
    yallow:                      rgb {hex_to_rgb(colors[10])};
    green:                       rgb {hex_to_rgb(colors[2])};
    lightfg:                     rgb {hex_to_rgb(colors[15])};
    lightbg:                     rgb {hex_to_rgb(colors[8])};
    foreground:                  rgb {hex_to_rgb(colors[7])};
    background:                  rgb {hex_to_rgb(colors[0])};
    background-color:            rgb {hex_to_rgb(colors[12])};
    }}
"""
    return rofi_config


config_path = f"{os.environ.get('HOME')}/.config"
colors = read_colors(colorscheme)
alacritty_config = generate_alacritty(colors)
bspwm_config = generate_bspwm(colors)
polybar_config = generate_polybar(colors)
rofi_config = generate_rofi(colors)

with open(config_path+"/alacritty/colors.toml", 'w') as f:
    f.write(alacritty_config)
with open(config_path+"/bspwm/colorsrc", 'w') as f:
    f.write(bspwm_config)
with open(config_path+"/polybar/polybar_colors.ini", 'w') as f:
    f.write(polybar_config)
with open(config_path+'/rofi/rofi_colors.rasi', 'w') as f:
    f.write(rofi_config)

print("Configuration files generated successfully!")
