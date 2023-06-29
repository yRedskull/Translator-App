from assets.py.translate import translate
from threading import Thread


def change_language_listener(self, get=None):

    if get == self.combobox_translator.get():
        self.combobox_translator.set(self.lang_before_listener)
        trade_text(self)
    else:
        Thread(target=lambda: release_translation_listener(self)).start()

    self.lang_before_listener = get


def change_language_translator(self, get=None):
    if get == self.combobox_listener.get():
        self.combobox_listener.set(self.lang_before_translator)
        trade_text(self)
    else:
        Thread(target=lambda: release_translation_translator(self)).start()

    self.lang_before_translator = get


def trade_text(self):
    self.textbox_translator.configure(state="normal")
    translator = self.textbox_translator.get("0.0", "end").replace("\n", "")
    listener = self.textbox_listener.get("0.0", "end").replace("\n", "")
    if listener and translator:
        self.textbox_translator.delete("0.0", "end")
        self.textbox_translator.insert("0.0", listener)
        self.textbox_translator.configure(state="disabled")
        self.textbox_listener.delete("0.0", "end")
        self.textbox_listener.insert("0.0", translator)


def release_translation_listener(self, text=None):
    text_translated = translate(text or self.textbox_listener.get("0.0", "end"),
                                lang_translator=self.combobox_listener.get())
    self.textbox_listener.delete("0.0", "end")
    self.textbox_listener.insert("0.0", text_translated)


def release_translation_translator(self, text=None):
    text_translated = translate(text or self.textbox_listener.get("0.0", "end"),
                                lang_translator=self.combobox_translator.get())
    self.textbox_translator.configure(state="normal")
    self.textbox_translator.delete("0.0", "end")
    self.textbox_translator.insert("0.0", text_translated)
    self.textbox_translator.configure(state="disabled")
