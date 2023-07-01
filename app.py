from customtkinter import *

from CTkScrollableDropdown import CTkScrollableDropdown

from navbar import NavBar

from assets.py.load_img import ImagesLoad
from assets.py.var import DEFAULT_LISTENER, DEFAULT_TRANSLATOR, LANGS_TRANSLATE
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
        self.resizable(True, True)
        self.minsize(620, 430)

        self.navbar = NavBar(self, corner_radius=0)
        self.navbar.pack(side="top", fill=X)

        self.div_listener = CTkFrame(self, fg_color=self.cget("fg_color"))
        self.div_listener.pack(side="left", fill=BOTH, expand=True, padx=2)

        self.combobox_listener = CTkComboBox(self.div_listener, width=300, cursor="hand2", state="readonly", justify="center", font=("Roboto", 20), corner_radius=5)
        self.combobox_listener.pack(pady=5)
        self.dropdown_listener = CTkScrollableDropdown(self.combobox_listener, values=list(LANGS_TRANSLATE.keys()), width=300, frame_corner_radius=5,
                                                       command=lambda get: change_language_listener(self, get), height=600, button_height=30)
        self.combobox_listener.set(DEFAULT_LISTENER)

        def paste_listener(event):
            def auto_detect():
                listener = self.textbox_listener.get("0.0", "end").replace("\n", "")
                translator = translate()
                detect = translator.detect(listener)

                for key in LANGS_TRANSLATE.keys():
                    if detect.lang == LANGS_TRANSLATE[key]:
                        if key == self.combobox_translator.get():
                            self.combobox_translator.set(self.combobox_listener.get())

                        self.combobox_listener.set(key)
                        break

            self.combobox_listener.after(300, Thread(target=auto_detect).start())
            self.textbox_listener.after(600, Thread(target=lambda: release_translation_translator(self)).start())

            return event

        def key_release_listener(event):
            def resolve():
                self.textbox_translator.configure(state="normal")
                self.textbox_translator.delete("0.0", "end")
                self.textbox_translator.configure(state="normal")
                Thread(target=lambda: release_translation_translator(self)).start()

            if self.after_id:
                self.after_cancel(self.after_id)
            self.after_id = self.after(400, resolve)
            return event

        self.textbox_listener = CTkTextbox(self.div_listener, height=450, wrap="word")
        self.textbox_listener.bind("<Control-v>", paste_listener)
        self.textbox_listener.bind("<KeyRelease>", key_release_listener)
        self.textbox_listener.pack(fill=BOTH, expand=True)

        self.div_translator = CTkFrame(self, fg_color=self.cget("fg_color"))
        self.div_translator.pack(side="left", fill=BOTH, expand=True, padx=2)

        self.combobox_translator = CTkComboBox(self.div_translator, width=300, cursor="hand2", state="readonly", justify="center", font=("Roboto", 20), corner_radius=5)
        self.combobox_translator.pack(pady=5)
        self.dropdown_translator = CTkScrollableDropdown(self.combobox_translator, values=list(LANGS_TRANSLATE.keys()), width=300, frame_corner_radius=5,
                                                         command=lambda get: change_language_translator(self, get), height=600, button_height=30)
        self.combobox_translator.set(DEFAULT_TRANSLATOR)

        self.textbox_translator = CTkTextbox(self.div_translator, state="disabled", height=450, wrap="word")
        self.textbox_translator.pack(fill=BOTH, expand=True)

        self.protocol("WM_DELETE_WINDOW", self.exit)

    def exit(self):
        fade_out(self)
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
