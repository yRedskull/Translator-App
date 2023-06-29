from customtkinter import CTkImage
from PIL import Image
from os import path


class ImagesLoad:
    def __init__(self):
        self.path_imgs = path.join(path.dirname(path.dirname(__file__)), "images")
        self.logo_bitmap = path.join(self.path_imgs, "translator.ico")
        self.logo_png = CTkImage(Image.open(path.join(self.path_imgs, "translator.png")), size=(64, 64))
        self.equal_light_png = CTkImage(Image.open(path.join(self.path_imgs, "equal-light.png")), size=(48, 48))
        self.equal_dark_png = CTkImage(Image.open(path.join(self.path_imgs, "equal-dark.png")), size=(48, 48))
