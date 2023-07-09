from customtkinter import CTkImage
from PIL import Image
from os import path


class ImagesLoad:
    def __init__(self):
        self.path_imgs = path.join(path.dirname(path.dirname(__file__)), "images")
        self.logo_bitmap = path.join(self.path_imgs, "translator.ico")
        self.logo_png = CTkImage(Image.open(path.join(self.path_imgs, "translator.png")), size=(64, 64))