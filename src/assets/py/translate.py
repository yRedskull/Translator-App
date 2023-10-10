from deep_translator import GoogleTranslator as Translator

from src.assets.py.var import LANGS_TRANSLATE


def translate(text, lang_translator):
    src, target = "auto", LANGS_TRANSLATE[lang_translator]
    translator = Translator(src=src, target=target)
    text_translated = None

    if text:
        try:
            text_translated = translator.translate(text)
        except:

            text_translated = None
        finally:
            return text_translated or text
    else:
        return translator
