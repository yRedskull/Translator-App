import os
import json
from deep_translator import GoogleTranslator


LANGS_TRANSLATE = GoogleTranslator().get_supported_languages(as_dict=True)

try:
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "json", "lang.json"), "r") as lang:
        loads = json.loads(lang.read())
        DEFAULT_LISTENER = loads["default_listener"]
        DEFAULT_TRANSLATOR = loads["default_translator"]
        DEFAULT_SYSTEM = loads["default_system"]
except Exception as e:
    DEFAULT_LISTENER = "english"
    DEFAULT_TRANSLATOR = "portuguese"
    DEFAULT_SYSTEM = "portuguese"

