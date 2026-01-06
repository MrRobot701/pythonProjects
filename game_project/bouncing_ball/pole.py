class Pole:
    def __init__(self, canvas, clr):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=clr)
        self.canvas.move(self.id, 200, 485)
        self.a = 0
        self.is_paused = False
        self.cvs_width = canvas.winfo_width()
        self.canvas.bind_all("<Left>", self.turn_left)
        self.canvas.bind_all("<Right>", self.turn_right)
        self.canvas.bind_all("<space>", self.pause)

    def draw(self):
        push = self.canvas.coords(self.id)
        # print(pos)
        if push[0] + self.a <= 0:
            self.a = 0
        if push[2] + self.a >= self.cvs_width:
            self.a = 0
        self.canvas.move(self.id, self.a, 0)

    def turn_left(self, event):
        self.a = -3.5

    def turn_right(self, event):
        self.a = 3.5

    def pause(self, event):
        self.is_paused = not self.is_paused
