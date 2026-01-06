from tkinter import *
import time
import random

from bouncing_ball.ball import Ball
from bouncing_ball.stone import Stone
from bouncing_ball.pole import Pole

root = Tk()
root.title("Bounce Ball Game")
root.geometry("500x570")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
canvas = Canvas(root, width=500, height=500, bd=0, highlightthickness=0, highlightbackground="Red", bg="Black")
canvas.pack(padx=10, pady=10)
score_label = Label(height=50, width=80, text="Score: 00", font="Calibri 14 italic")
score_label.pack(side="left")
root.update()


def start_game(event):
    score_label.configure(text="Score: 00")
    canvas.delete("all")
    BALL_COLOR = ["blue", "green", "violet"]
    STONE_COLOR = ["green", "dark blue", "red", "pink", "violet", "yellow",
                   "orange", "gray", "brown", "white", "blue", "yellow green",
                   "navajo white", "dark gray", "violet red", "powder blue", "blue violet"]
    pole = Pole(canvas, "yellow")
    stones = []
    for i in range(0, 5):
        b = []
        for j in range(0, 19):
            tmp = Stone(canvas, random.choice(STONE_COLOR))
            b.append(tmp)
        stones.append(b)

    for i in range(0, 5):
        for j in range(0, 19):
            canvas.move(stones[i][j].id, 25 * j, 25 * i)

    ball = Ball(canvas, random.choice(BALL_COLOR), pole, stones, score_label)
    root.update_idletasks()
    root.update()

    time.sleep(1)
    while True:
        if pole.is_paused:
            try:
                canvas.delete(m)
                del m
            except:
                pass
            if not ball.bottom_hit:
                ball.draw()
                pole.draw()
                root.update_idletasks()
                root.update()
                time.sleep(0.01)
                if ball.hit == 95:
                    canvas.create_text(250, 250, text="YOU WON !!", fill="yellow", font="Calibri 24 ")
                    root.update_idletasks()
                    root.update()
                    break
            else:
                canvas.create_text(250, 250, text="GAME OVER!!", fill="red", font="Calibri 24 ")
                root.update_idletasks()
                root.update()
                break
        else:
            try:
                if m is None: pass
            except:
                m = canvas.create_text(250, 250, text="PAUSE!!", fill="green", font="Calibri 24 ")
            root.update_idletasks()
            root.update()


root.bind_all("<Return>", start_game)
canvas.create_text(250, 250, text="Press Enter to start Game!!", fill="yellow", font="Calibri 18")
root.mainloop()
