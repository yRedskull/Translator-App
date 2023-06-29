from customtkinter import CTkFont

import os
import json


def config_font(self):
    try:
        with open(os.path.join(os.path.dirname(__file__), "assets", "json", "custom_font.json"), "r") as custom_font:
            font = json.loads(custom_font.read())
            self.font = CTkFont(family=font["family"], size=font["size"],
                                weight=font["weight"], slant=font["slant"],
                                underline=font["underline"], overstrike=font["overstrike"])
    except:
        self.font = {
            "family": "Roboto",
            "size": 18,
            "weight": "normal",
            "slant": "roman",
            "underline": False,
            "overstrike": False
        }
