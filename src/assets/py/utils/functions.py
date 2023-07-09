from src.assets.py.translate import translate

from threading import Thread

from time import sleep as sl


def change_language_listener(self, get=None):
    listener = self.textbox_listener.get("0.0", "end").replace("\n", "")
    translator = self.textbox_translator.get("0.0", "end").replace("\n", "")

    if get == self.combobox_translator.get():
        self.combobox_translator.set(self.combobox_listener.get())

        if listener and translator:
            trade_text(self, listener, translator)

    if listener and translator:
        Thread(target=lambda: self.combobox_listener.after(100, release_translation_listener(self))).start()

    return self.combobox_listener.set(get)


def change_language_translator(self, get=None):
    listener = self.textbox_listener.get("0.0", "end").replace("\n", "")
    translator = self.textbox_translator.get("0.0", "end").replace("\n", "")

    if get == self.combobox_listener.get():
        self.combobox_listener.set(self.combobox_translator.get())

        if listener and translator:
            trade_text(self, listener, translator)

    if listener and translator:
        Thread(target=lambda: self.combobox_translator.after(100, release_translation_translator(self))).start()

    return self.combobox_translator.set(get)


def trade_text(self, listener, translator):
    self.textbox_translator.configure(state="normal")
    self.textbox_translator.delete("0.0", "end")
    self.textbox_translator.insert("0.0", listener)
    self.textbox_translator.configure(state="disabled")
    self.textbox_listener.delete("0.0", "end")
    self.textbox_listener.insert("0.0", translator)

    return listener, translator


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


def fade_out(self):
    for i in range(100, 0, -10):
        if not self.winfo_exists():
            break
        self.attributes("-alpha", i / 100)
        self.update()
        sl(1 / 100)

    self.attributes("-alpha", 0)


def fade_in(self):
    for i in range(0, 100, 10):
        if not self.winfo_exists():
            break
        self.attributes("-alpha", i / 100)
        self.update()
        sl(1 / 100)

    self.attributes("-alpha", 1)
