from customtkinter import *

from navbar import NavBar

from assets.py.load_img import ImagesLoad
from assets.py.var import *
from assets.py.utils.functions import *

from os import path


class App(CTk):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # VAR
        self.combobox_translator = None
        self.combobox_listener = None
        self.after_id = None

        self.images = ImagesLoad()

        set_default_color_theme(path.join(path.dirname(__file__), "assets", "json", "custom_theme.json"))

        self.title("Translator App")
        self.wm_iconbitmap(self.images.logo_bitmap)

        self.width_screen = self.winfo_screenwidth()
        self.height_screen = self.winfo_screenheight()
        self.win_width = 800
        self.win_height = 480
        width_plus = (self.width_screen // 2 - self.win_width // 2)
        height_plus = (self.height_screen // 2 - self.win_height // 2)
        self.geometry(f"{self.win_width}x{self.win_height}+{width_plus}+{height_plus}")
        self.resizable(True, False)
        self.minsize(520, 0)

        self.navbar = NavBar(self, corner_radius=0)
        self.navbar.pack(side="top", fill=X)

        self.div_center = CTkFrame(self, corner_radius=0, fg_color=self.cget("fg_color"))
        self.div_center.pack(fill=BOTH, expand=True, pady=5)

        self.div_listener = CTkFrame(self.div_center, fg_color=self.div_center.cget("fg_color"))
        self.div_listener.pack(side="left", fill=BOTH, expand=True, padx=2)

        self.lang_before_listener = DEFAULT_LISTENER
        self.combobox_listener = CTkComboBox(self.div_listener, values=list(LANGS_TRANSLATE.keys()), width=200,
                                             state="readonly", cursor="hand2", command=lambda get: change_language_listener(self, get))
        self.combobox_listener.set(DEFAULT_LISTENER)
        self.combobox_listener.pack()

        def paste_listener(event):
            Thread(target=lambda: self.textbox_listener.after(200, lambda: release_translation_translator(self))).start()
            return event

        def key_release_listener(event):
            def resolve():
                self.textbox_translator.configure(state="normal")
                self.textbox_translator.delete("0.0", "end")
                self.textbox_translator.configure(state="normal")
                Thread(target=lambda: release_translation_translator(self)).start()

            if hasattr(self, 'after_id') and self.after_id is not None:
                self.after_cancel(self.after_id)
            self.after_id = self.after(300, resolve)

        self.textbox_listener = CTkTextbox(self.div_listener, height=450, wrap="word")
        self.textbox_listener.bind("<Control-v>", paste_listener)
        self.textbox_listener.bind("<KeyRelease>", key_release_listener)
        self.textbox_listener.pack(fill=BOTH)

        self.div_translator = CTkFrame(self.div_center, fg_color=self.div_center.cget("fg_color"))
        self.div_translator.pack(side="left", fill=BOTH, expand=True, padx=2)

        self.lang_before_translator = DEFAULT_TRANSLATOR
        self.combobox_translator = CTkComboBox(self.div_translator, values=list(LANGS_TRANSLATE.keys()), width=200,
                                               state="readonly", cursor="hand2",
                                               command=lambda get: change_language_translator(self, get))
        self.combobox_translator.set(DEFAULT_TRANSLATOR)
        self.combobox_translator.pack()

        self.textbox_translator = CTkTextbox(self.div_translator, state="disabled", height=450, wrap="word")
        self.textbox_translator.pack(fill=BOTH)

        self.after_idle(self.update)


if __name__ == "__main__":
    app = App()
    app.mainloop()
