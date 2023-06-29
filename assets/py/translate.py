from googletrans import Translator

from assets.py.var import LANGS_TRANSLATE, DEFAULT_SYSTEM


def listener_for_translator(translator):
    source = "auto"

    if translator:
        destiny = LANGS_TRANSLATE[translator]
    else:
        destiny = LANGS_TRANSLATE[DEFAULT_SYSTEM]

    return source, destiny


def translate(text, lang_translator=None):
    translator = Translator()
    text_translated = None
    src, dest = listener_for_translator(lang_translator)

    try:
        text_translated = translator.translate(text, src=src, dest=dest).text
    except:
        text_translated = None
    finally:
        return text_translated or text

