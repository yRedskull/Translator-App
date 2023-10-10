from src.assets.py.translate import translate

from time import sleep as sl


def select_dropdown_language(self, shooter, target, get=None):
    if get == target.get():
        target.set(shooter.get())
        trade_text(self)

    shooter.set(get)

    if shooter == self.combobox_translator:
        show_translation()


def inverter_languages(self):
    change_listener = self.combobox_translator.get()
    change_translator = self.combobox_listener.get()

    self.combobox_listener.set(change_listener)
    self.combobox_translator.set(change_translator)
    trade_text(self)


def trade_text(self):
    listener = self.textbox_listener.get("0.0", "end").replace("\n", "")
    translator = self.textbox_translator.get("0.0", "end").replace("\n", "")

    self.textbox_translator.configure(state="normal")
    self.textbox_translator.delete("0.0", "end")
    self.textbox_translator.insert("0.0", listener)
    self.textbox_translator.configure(state="disabled")
    self.textbox_listener.delete("0.0", "end")
    self.textbox_listener.insert("0.0", translator)

    return listener, translator


def show_translation(self, text=None):
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
