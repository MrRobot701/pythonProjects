import random
import time

from tkinter import *
from settings import Setting

from bouncing_ball_2.pole import Pole
from bouncing_ball_2.stone import Stone
from bouncing_ball_2.ball import Ball


class Game:

    def __init__(self):
        self.__settings = Setting()

        self.__root = Tk()
        self.__root.title(self.__settings.GAME_TITLE)
        self.__root.geometry(self.__settings.RESOLUTION)
        self.__root.resizable(0, 0)
        self.__root.wm_attributes("-topmost", 1)

        w = self.__settings.CANVAS_WIDTH
        h = self.__settings.CANVAS_HEIGHT
        self.__canvas = Canvas(self.__root, width=w, height=h, bd=0, highlightthickness=0,
                               highlightbackground="Red", bg="Black")
        self.__canvas.pack(padx=10, pady=10)
        self.__score_label = Label(height=50, width=80, text=self.__settings.SCORE_TEXT, font="Calibri 14 italic")
        self.__score_label.pack(side="left")
        self.__root.update()

    def start(self):
        self.__root.bind_all("<Return>", self.__start_game)
        self.__canvas.create_text(250, 250, text="Press Enter to start Game!!", fill="yellow", font="Calibri 18")
        self.__root.mainloop()

    def __start_game(self, event):
        self.__canvas.delete("all")

        pole = Pole(self.__canvas, random.choice(self.__settings.COLORS))
        stones = Stone.set_stones(self.__canvas, self.__settings.COLORS)
        ball = Ball(self.__canvas, random.choice(self.__settings.COLORS), pole, stones, self.__score_label)

        self.__start_game_loop(pole, ball)

    def __start_game_loop(self, pole, ball):
        m = None
        while True:
            if not pole.is_paused:
                if m is not None:
                    self.__canvas.delete(m)
                    m = None
                if not ball.bottom_hit:
                    ball.draw()
                    pole.draw()
                    self.__update_screen()
                    time.sleep(0.01)
                    if ball.hit == 95:
                        self.__canvas.create_text(250, 250, text=self.__settings.YOU_WON_TEXT,
                                                  fill="yellow", font="Calibri 24 ")
                        self.__update_screen()
                        break
                else:
                    self.__canvas.create_text(250, 250, text=self.__settings.GAME_OVER_TEXT,
                                              fill="red", font="Calibri 24 ")
                    self.__update_screen()
                    break
            else:
                if m is None:
                    m = self.__canvas.create_text(250, 250, text="PAUSE!!", fill="green", font="Calibri 24 ")
                self.__update_screen()

    def __update_screen(self):
        self.__root.update_idletasks()
        self.__root.update()
