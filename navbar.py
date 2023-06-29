from customtkinter import CTkSwitch, CTkFrame, get_appearance_mode, set_appearance_mode, StringVar


class NavBar(CTkFrame):

    def __init__(self, master, *args, **kwargs):

        super().__init__(master, *args, **kwargs)

        def switch_theme():
            set_appearance_mode(switch_theme_mode.get())
            self.btn_mode.configure(text=get_appearance_mode())

        def offvaluetheme():
            if get_appearance_mode() == "Dark":
                return "light"
            elif get_appearance_mode() == "Light":
                return "dark"

        value_off = offvaluetheme()
        switch_theme_mode = StringVar(value=get_appearance_mode())
        self.btn_mode = CTkSwitch(self, text=get_appearance_mode(), variable=switch_theme_mode, command=switch_theme, onvalue=get_appearance_mode(), offvalue=value_off)
        self.btn_mode.pack(anchor="e")
