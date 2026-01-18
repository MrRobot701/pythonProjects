import tkinter
from unit import Unit
from settings import Setting


class Game:

    def __init__(self, title):
        self.settings = Setting()
        w = self.settings.width
        h = self.settings.height
        color = self.settings.bg_color
        self.__frame = tkinter.Tk()
        self.__frame.geometry(self.settings.resolution)
        self.__frame.title(title)
        canvas = tkinter.Canvas(self.__frame, width=w, height=h, bg=color)
        canvas.pack()

    def start(self):
        self.__frame.mainloop()

    def __set_up_game(self):
        self.__player = Unit(100, 0, 0, 10)
