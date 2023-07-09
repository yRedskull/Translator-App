from src.assets.py.var import LANGS_TRANSLATE
from src.assets.py.utils.functions import translate, Thread, release_translation_translator


def paste_listener(self):
    def auto_detect():
        listener = self.textbox_listener.get("0.0", "end").replace("\n", "")
        translator = translate()
        detect = translator.detect(listener)
        if listener:
            for key in LANGS_TRANSLATE.keys():
                if detect.lang == LANGS_TRANSLATE[key]:
                    if key == self.combobox_translator.get():
                        self.combobox_translator.set(self.combobox_listener.get())

                    self.combobox_listener.set(key)
                    break

    self.combobox_listener.after(400, auto_detect)
    Thread(target=lambda: self.textbox_listener.after(600, release_translation_translator(self))).start()


def key_release_listener(self):
    listener = self.textbox_listener.get("0.0", "end").replace("\n", "")
    if listener:
        def resolve():
            self.textbox_translator.configure(state="normal")
            self.textbox_translator.delete("0.0", "end")
            self.textbox_translator.configure(state="normal")
            Thread(target=lambda: release_translation_translator(self)).start()

        if self.after_id:
            self.after_cancel(self.after_id)
        self.after_id = self.after(400, resolve)
