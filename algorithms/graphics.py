from tkinter import *


class Graphics:

    def __init__(self, width, height, bg_color):
        self.__color = "black"
        self.__frame = Tk()
        self.canvas = Canvas(self.__frame, width=width, height=height, bg=bg_color)
        self.canvas.pack()

    def set_color(self, color):
        self.__color = color

    def draw_pixel(self, x, y):
        self.canvas.create_line(x, y, x + 1, y, fill=self.__color)

    def draw_line(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        if abs(dx) >= abs(dy):
            k = dy / dx
            for x in range(x1, x2 + 1):
                y = round(k * (x - x1)) + y1
                self.draw_pixel(x, y)
        else:
            k = dx / dy
            for y in range(y1, y2 + 1):
                x = round(k * (y - y1)) + x1
                self.draw_pixel(x, y)

    def draw_line_out_of_box(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, fill=self.__color)

    def fill_rectangle(self, x1, y1, width, height):
        for x in range(x1, x1 + width + 1):
            self.draw_line(x, y1, x, y1 + height)

    def fill_rectangle_pixel(self, x1, y1, width, height):
        for x in range(x1, x1 + width + 1):
            for y in range(y1, y1 + height + 1):
                self.draw_pixel(x, y)

    def init(self):
        self.__frame.mainloop()
