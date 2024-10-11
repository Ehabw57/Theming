#!/usr/bin/python
from sys import argv
import json
import os
import requests

theme_sources = {'alacritty': "tinted-theming/tinted-alacritty/master/colors/base16-"}


class ThemeDownloader:
    def __init__(self, theme_name=None):
        self.name = theme_name
        self.base_url = "https://raw.githubusercontent.com/"

    def download_theme(self):
        """ Download a theme from a URL and save it to a file """
        url = self.base_url + theme_sources['alacritty'] + self.name + ".toml"

        response = requests.get(url)
        if response.status_code != 200:
            print(url)
            print(f"Failed to download code {response.status_code}")
            return 1
        if not os.path.exists("./colors"):
            print("colors dir not presetnt")
            exit(0)

        with open(f"colors/{self.name}", "wb") as file:
            file.write(response.content)


theme_maneger = ThemeDownloader()

with open("themes", "r") as file:
    theme_maneger.themes = json.load(file)

# if the script is run without any arguments, list available themes
if len(argv) < 2:
    for theme in theme_maneger.themes:
        print(theme)
    exit(1)


theme_maneger.name = argv[1]
if theme_maneger.name not in theme_maneger.themes:
    print(f"Error: {theme_maneger.name} is not a valid theme")
    exit(1)

if not theme_maneger.download_theme():
    print(f"Downloaded {theme_maneger.name} theme")
else:
    print(f"Error: Could not download {theme_maneger.name} theme")
