from customtkinter import CTkFont

import os
import json


def config_font(self):
    try:
        with open(os.path.join(os.path.dirname(__file__), "assets", "json", "custom_font.json"), "r") as custom_font:
            fonts = json.loads(custom_font.read())
            textbox = fonts["Textbox"]
            self.font_textbox = CTkFont(family=textbox["family"], size=textbox["size"],
                                        weight=textbox["weight"], slant=textbox["slant"],
                                        underline=textbox["underline"], overstrike=textbox["overstrike"])
            self.font_combobox = CTkFont()
    except:
        self.font_textbox = {
            "family": "Roboto",
            "size": 18,
            "weight": "normal",
            "slant": "roman",
            "underline": False,
            "overstrike": False
        }
