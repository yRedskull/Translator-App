import os
import json


LANGS_TRANSLATE = {
                    "Português": "pt",

                    "Inglês": "en",

                    "Francês": "fr",

                    "Chinês (Simplificado)": "zh-cn",

                    "Chinês (Tradicional)": "zh-tw",

                    "Ucraniano": "uk",

                    "Italiano": "it",

                    "Alemão": "de",

                    "Espanhol": "es",

                    "Russo": "ru"
}

try:
    with open(os.path.join(os.path.dirname(__file__), "assets", "json", "lang.json"), "r") as lang:
        loads = json.loads(lang.read())
        DEFAULT_LISTENER = loads["default_listener"]
        DEFAULT_TRANSLATOR = loads["default_translator"]
        DEFAULT_SYSTEM = loads["default_system"]
except:
    DEFAULT_LISTENER = "Português"
    DEFAULT_TRANSLATOR = "Inglês"
    DEFAULT_SYSTEM = "Português"

