from customtkinter import CTkSwitch, CTkFrame, get_appearance_mode, set_appearance_mode, StringVar, CTkButton
from src.assets.py.utils.functions import fade_out, fade_in, inverter_languages
from threading import Thread


class NavBar(CTkFrame):

    def __init__(self, master, *args, **kwargs):

        super().__init__(master, *args, **kwargs)

        def switch_theme():
            fade_out(master)
            switch = Thread(target=set_appearance_mode(switch_theme_mode.get()))
            switch.start()
            switch.join()
            fade_in(master)
            self.btn_mode.configure(text=get_appearance_mode())

        def offvaluetheme():
            if get_appearance_mode() == "Dark":
                return "light"
            else:
                return "dark"

        value_off = offvaluetheme()
        switch_theme_mode = StringVar(value=get_appearance_mode())

        ghost_btn = CTkButton(self, text="", fg_color=self.cget("fg_color"), border_width=0, hover=False, width=100)
        ghost_btn.pack(expand=True, side="left")

        self.btn_trade = CTkButton(self, text="⇄", font=("Arial", 30), width=50, corner_radius=40, border_width=0,
                                   command=lambda: inverter_languages(master))
        self.btn_trade.pack(expand=True, side="left")

        self.btn_mode = CTkSwitch(self, text=get_appearance_mode(), variable=switch_theme_mode, command=switch_theme, onvalue=get_appearance_mode(), offvalue=value_off)
        self.btn_mode.pack(side="left", expand=True)


