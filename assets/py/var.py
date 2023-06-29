import os
import json


LANGS_TRANSLATE = {
                    "Português": "portuguese",

                    "Inglês": "english",

                    "Francês": "french",

                    "Chinês (Simplificado)": "chinese (simplified)",

                    "Chinês (Tradicional)": "chinese (traditional)",

                    "Ucraniano": "ukrainian",

                    "Italiano": "italian",

                    "Alemão": "german",

                    "Espanhol": "spanish",

                    "Russo": "russian"
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

