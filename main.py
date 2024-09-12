#!/usr/bin/python
from os import makedirs as mkdir
from sys import argv
import json
from os.path import exists
from theme_downloader import ThemeDownloader
from config import theme_configurations


theme_maneger = ThemeDownloader()

# if the avalible themes file does not exist, create it
if not exists("themes"):
    theme_maneger.get_theme_names()

with open("themes", "r") as file:
    theme_maneger.themes = json.load(file)

# if the script is run without any arguments, list available themes
if len(argv) < 2:
    for theme in theme_maneger.themes:
        print(theme)
    exit(1)


theme_maneger.name = argv[1]
if theme_maneger.name not in theme_maneger.themes:
    print(theme_maneger.themes)
    print(f"Error: {theme_maneger.name} is not a valid theme")
    exit(1)

if not exists(theme_maneger.name):
    mkdir(theme_maneger.name, exist_ok=True)


for theme_type, file_extension, output in theme_configurations:
    file_path = f"{theme_maneger.name}/{output}"
    if not exists(file_path):
        if not theme_maneger.download_theme(theme_type, file_extension, output):
            print(f"Downloaded {theme_type} theme")
        else:
            print(f"Error: Could not download {theme_type} theme")
