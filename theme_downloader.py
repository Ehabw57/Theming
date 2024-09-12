#!/usr/bin/env python
""" A script to download and save base16 themes """
import requests
import json
from config import theme_sources


class ThemeDownloader:
    """ A class to download and save various themes """

    def __init__(self, theme_name=None):
        self.name = theme_name
        self.base_url = "https://raw.githubusercontent.com/"
        self.themes = []

    def get_theme_names(self):
        """ Get the names of the available themes """
        url = "https://api.github.com/repos/tinted-theming/base16-i3/contents/colors"
        respond = requests.get(url)

        # get the theme names from the response
        for obj in respond.json():
            for key, value in obj.items():
                if key == "name":
                    self.themes.append(value[7:-7])
        # write the theme names to the themes file
        with open("themes", "w") as file:
            json.dump(self.themes, file)

    def download_theme(self, theme_type, file_extension, output_filename):
        """ Download a theme from a URL and save it to a file """
        base_url = theme_sources.get(theme_type)

        url = self.base_url + base_url + self.name + file_extension

        response = requests.get(url)
        if response.status_code != 200:
            return 1

        with open(f"{self.name}/{output_filename}", "wb") as file:
            file.write(response.content)
