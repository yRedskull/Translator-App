from customtkinter import *

from CTkScrollableDropdown import CTkScrollableDropdown

try:
    from frontend.navbar import NavBar
except:
    from navbar import NavBar

from src.assets.py.load_img import ImagesLoad
from src.assets.py.var import DEFAULT_LISTENER, DEFAULT_TRANSLATOR, LANGS_TRANSLATE
from src.assets.py.utils.functions import select_dropdown_language, fade_out
from src.assets.py.utils.listener import paste_listener, key_release_listener

from os import path


class App(CTk):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # VAR
        self.div_trade = None
        self.btn_trade = None
        self.textbox_translator = None
        self.dropdown_translator = None
        self.div_translator = None
        self.dropdown_listener = None
        self.textbox_listener = None
        self.div_listener = None
        self.navbar = None
        self.combobox_translator = None
        self.combobox_listener = None
        self.after_id = None

        self.images = ImagesLoad()

        set_default_color_theme(path.join(path.dirname(__file__), "../src/assets", "json", "custom_theme.json"))

        self.title("Translator App")
        self.wm_iconbitmap(self.images.logo_bitmap)

        self.width_screen = self.winfo_screenwidth()
        self.height_screen = self.winfo_screenheight()
        self.win_width = 800
        self.win_height = 480
        width_plus = (self.width_screen // 2 - self.win_width // 2)
        height_plus = (self.height_screen // 2 - self.win_height // 2)
        self.geometry(f"{self.win_width}x{self.win_height}+{width_plus}+{height_plus}")
        self.resizable(True, True)
        self.minsize(620, 430)

        self.after_idle(self.components)

        self.protocol("WM_DELETE_WINDOW", self.exit)

    def components(self):
        self.navbar = NavBar(self, corner_radius=0)
        self.navbar.pack(side="top", fill=X)

        self.div_listener = CTkFrame(self, fg_color=self.cget("fg_color"))
        self.div_listener.pack(side="left", fill=BOTH, expand=True, padx=2)

        self.combobox_listener = CTkComboBox(self.div_listener, width=300, cursor="hand2", state="readonly",
                                             justify="center", font=("Roboto", 20), corner_radius=5)
        self.combobox_listener.pack(pady=5)
        self.dropdown_listener = CTkScrollableDropdown(self.combobox_listener, values=list(LANGS_TRANSLATE.keys()),
                                                       width=300, frame_corner_radius=5,
                                                       command=lambda get: select_dropdown_language(self, self.combobox_listener,
                                                                                                    self.combobox_translator, get=get),
                                                       height=350, button_height=30)
        self.combobox_listener.set(DEFAULT_LISTENER)

        self.textbox_listener = CTkTextbox(self.div_listener, height=450, wrap="word")
        self.textbox_listener.bind("<Control-v>", lambda e: paste_listener(self))
        self.textbox_listener.bind("<KeyRelease>", lambda e: key_release_listener(self))
        self.textbox_listener.pack(fill=BOTH, expand=True)

        self.div_translator = CTkFrame(self.div_trade, fg_color=self.cget("fg_color"))
        self.div_translator.pack(side="left", fill=BOTH, expand=True, padx=2)

        self.combobox_translator = CTkComboBox(self.div_translator, width=300, cursor="hand2", state="readonly",
                                               justify="center", font=("Roboto", 20), corner_radius=5)
        self.combobox_translator.pack(pady=5)
        self.dropdown_translator = CTkScrollableDropdown(self.combobox_translator, values=list(LANGS_TRANSLATE.keys()),
                                                         width=300, frame_corner_radius=5,
                                                         command=lambda get: select_dropdown_language(self, self.combobox_translator, self.combobox_listener, get),
                                                         height=350, button_height=30)
        self.combobox_translator.set(DEFAULT_TRANSLATOR)

        self.textbox_translator = CTkTextbox(self.div_translator, state="disabled", height=450, wrap="word")
        self.textbox_translator.pack(fill=BOTH, expand=True)

    def exit(self):
        fade_out(self)
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
